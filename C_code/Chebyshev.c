#include <stdio.h>
#include <math.h>

#define NPTS 100

double* chebspace(int npts) {
    double* t = (double*)malloc(npts * sizeof(double));
    for (int i = 0; i < npts; ++i) {
        t[i] = -cos((i + 0.5) * M_PI / npts);
    }
    return t;
}

double** chebmat(double* u, int N) {
    double** T = (double**)malloc(N * sizeof(double*));
    for (int i = 0; i < N; ++i) {
        T[i] = (double*)malloc(N * sizeof(double));
    }

    for (int i = 0; i < N; ++i) {
        T[i][0] = 1.0;
        T[i][1] = u[i];
    }

    for (int n = 2; n < N; ++n) {
        for (int i = 0; i < N; ++i) {
            T[i][n] = 2.0 * u[i] * T[i][n - 1] - T[i][n - 2];
        }
    }

    return T;
}

typedef struct {
    double c;
    double m;
    double* coeffs;
} Cheby;

Cheby* create_cheby(double a, double b, double* coeffs, int num_coeffs) {
    Cheby* cheby = (Cheby*)malloc(sizeof(Cheby));
    cheby->c = (a + b) / 2.0;
    cheby->m = (b - a) / 2.0;
    cheby->coeffs = (double*)malloc(num_coeffs * sizeof(double));
    for (int i = 0; i < num_coeffs; ++i) {
        cheby->coeffs[i] = coeffs[i];
    }
    return cheby;
}

double rangestart(Cheby* cheby) {
    return cheby->c - cheby->m;
}

double rangeend(Cheby* cheby) {
    return cheby->c + cheby->m;
}

void range(Cheby* cheby, double* start, double* end) {
    *start = rangestart(cheby);
    *end = rangeend(cheby);
}

int degree(Cheby* cheby) {
    return (int)(sizeof(cheby->coeffs) / sizeof(double)) - 1;
}

Cheby* truncate(Cheby* cheby, int n) {
    double* truncated_coeffs = (double*)malloc((n + 1) * sizeof(double));
    for (int i = 0; i <= n; ++i) {
        truncated_coeffs[i] = cheby->coeffs[i];
    }
    return create_cheby(rangestart(cheby), rangeend(cheby), truncated_coeffs, n + 1);
}

double* as_taylor(Cheby* cheby, double x0, double m0) {
    int n = degree(cheby) + 1;
    double* Tprev = (double*)calloc(n, sizeof(double));
    double* T = (double*)calloc(n, sizeof(double));
    Tprev[0] = 1.0;
    T[1] = 1.0;

    // Evaluate y = Chebyshev functions as polynomials in u
    double* y = (double*)malloc(n * sizeof(double));
    for (int i = 0; i < n; ++i) {
        y[i] = cheby->coeffs[0] * Tprev[i];
    }

    for (int j = 1; j < n; ++j) {
        for (int i = 0; i < n; ++i) {
            y[i] += T[i] * cheby->coeffs[j];
        }

        double* xT = (double*)malloc(n * sizeof(double));
        for (int i = 1; i < n; ++i) {
            xT[i] = T[i - 1];
        }
        xT[0] = 0;

        double* Tnext = (double*)malloc(n * sizeof(double));
        for (int i = 0; i < n; ++i) {
            Tnext[i] = 2.0 * xT[i] - Tprev[i];
        }

        free(Tprev);
        Tprev = T;
        T = Tnext;
    }

    // Now evaluate y2 = polynomials in x
    double* P = (double*)calloc(n, sizeof(double));
    double* y2 = (double*)calloc(n, sizeof(double));
    P[0] = 1.0;
    double k0 = -cheby->c / cheby->m;
    double k1 = 1.0 / cheby->m;
    k0 = k0 + k1 * x0;
    k1 = k1 / m0;

    for (int i = 0; i < n; ++i) {
        y2[i] = 0.0;
        for (int j = 0; j < n; ++j) {
            y2[i] += P[j] * y[j];
        }

        double* Pnext = (double*)malloc(n * sizeof(double));
        for (int j = 1; j < n; ++j) {
            Pnext[j] = P[j - 1] * k1;
        }
        Pnext[0] = 0;

        for (int j = 0; j < n; ++j) {
            Pnext[j] += k0 * P[j];
        }

        free(P);
        P = Pnext;
    }

    free(T);
    free(y);
    free(P);

    return y2;
}

double eval_cheby(Cheby* cheby, double x) {
    double u = (x - cheby->c) / cheby->m;
    double* Tprev = (double*)calloc(degree(cheby) + 1, sizeof(double));
    double* T = (double*)calloc(degree(cheby) + 1, sizeof(double));
    Tprev[0] = 1.0;

    double y = cheby->coeffs[0] * Tprev[0];

    if (degree(cheby) > 0) {
        y += u * cheby->coeffs[1];
        T[0] = u;
    }

    for (int n = 2; n <= degree(cheby); ++n) {
        double* Tnext = (double*)malloc((degree(cheby) + 1) * sizeof(double));
        for (int i = 0; i <= degree(cheby); ++i) {
            Tnext[i] = 2.0 * u * T[i] - Tprev[i];
        }

        free(Tprev);
        Tprev = T;
        T = Tnext;

        for (int i = 0; i <= degree(cheby); ++i) {
            y += T[i] * cheby->coeffs[n];
        }
    }

    free(T);
    free(Tprev);

    return y;
}

void free_cheby(Cheby* cheby) {
    free(cheby->coeffs);
    free(cheby);
}

Cheby* fit_cheby(double (*func)(double), double a, double b, int degree) {
    int N = degree + 1;
    double* u = chebspace(N);
    double* x = (double*)malloc(N * sizeof(double));
    for (int i = 0; i < N; ++i) {
        x[i] = (u[i] * (b - a) + (b + a)) / 2.0;
    }

    double* y = (double*)malloc(N * sizeof(double));
    for (int i = 0; i < N; ++i) {
        y[i] = func(x[i]);
    }

    double** T = chebmat(u, N);

    double* c = (double*)malloc(N * sizeof(double));
    for (int i = 0; i < N; ++i) {
        c[i] = 0.0;
        for (int j = 0; j < N; ++j) {
            c[i] += 2.0 / N * y[j] * T[j][i];
        }
    }
    c[0] /= 2.0;

    free(u);
    free(x);
    free(y);

    for (int i = 0; i < N; ++i) {
        free(T[i]);
    }
    free(T);

    return create_cheby(a, b, c, N);
}

int main() {
    // Example usage
    Cheby* cheby = fit_cheby(sin, -1.0, 1.0, 5);
    printf("Cheby range: [%f, %f]\n", rangestart(cheby), rangeend(cheby));

    double x = 0.5;
    printf("Cheby(%f) = %f\n", x, eval_cheby(cheby, x));

    free_cheby(cheby);

    return 0;
}
