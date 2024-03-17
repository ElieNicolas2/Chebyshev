module ChebyshevOptimized #(parameter logic [17:0] coef0 = 18'H82, coef1 = 18'H1cc8, coef2 = 18'H3df43, coef3 = 18'H1ec5, coef4 = 18'H3f4ab)
//(input logic [17:0] coef0, coef1, coef2, coef3, coef4,
(input logic [17:0] xin, input logic clk, async, output logic [17:0] yout);

logic [17:0] r_reg1, r_reg2_1, r_reg2_2, r_reg3_1, r_reg3_2, r_reg4_1, r_reg4_2, r_reg5_1, r_reg5_2, r_reg6_1, r_reg6_2, r_reg7_1, r_reg7_2, r_reg8_1;
logic [17:0] r_next2, r_next4, r_next6, r_next8;
logic [17:0] r_next1, r_next3, r_next5, r_next7; 
logic [35:0] r_temp1, r_temp2, r_temp3, r_temp4;

always_ff @(posedge clk)begin
if(async)begin
r_reg1 <= '0;
r_reg2_1 <= '0;
r_reg2_2 <= '0;
r_reg3_1 <= '0;
r_reg3_2 <= '0;
r_reg4_1 <= '0;
r_reg4_2 <= '0;
r_reg5_1 <= '0;
r_reg5_2 <= '0;
r_reg6_1 <= '0;
r_reg6_2 <= '0;
r_reg7_1 <= '0;
r_reg7_2 <= '0;
r_reg8_1 <= '0;
yout <= '0;
end
else
begin
r_reg1 <= xin;       // registering input : x
r_reg2_1 <= r_reg1;  // keeping x
r_reg2_2 <= r_next1; // a4*x
r_reg3_1 <= r_reg2_1;// keeping x
r_reg3_2 <= r_next2; // a4*x + a3
r_reg4_1 <= r_reg3_1;// keeping x
r_reg4_2 <= r_next3; // (a4*x + a3)*x
r_reg5_1 <= r_reg4_1;// keeping x
r_reg5_2 <= r_next4; // (a4*x + a3)*x + a2
r_reg6_1 <= r_reg5_1;// keeping x
r_reg6_2 <= r_next5; // ((a4*x + a3)*x + a2)*x
r_reg7_1 <= r_reg6_1;// keeping x
r_reg7_2 <= r_next6; // ((a4*x + a3)*x + a2)*x + a1
r_reg8_1 <= r_next7; // (((a4*x + a3)*x + a2)*x + a1)*x
yout <= r_next8;     // registering output : (((a4*x + a3)*x + a2)*x + a1)*x + a0
end
end

//Stage 1

multiplier mutiplier1(.clock(clk), .aclr(async), .dataa(r_reg1), .datab(coef4), .result(r_temp1)); //a4*x
//normmul multiplier1(.dataa(r_reg1), .datab(coef4), .result(r_temp1));
assign r_next1 = r_temp1[29:12];

//Stage 2

adder add1(.clock(clk), .aclr(async), .dataa(r_reg2_2), .datab(coef3), .result(r_next2)); // (a4*x + a3)
//normadd add1(.dataa(r_reg2_2), .datab(coef3), .result(r_next2));
//Stage 3

multiplier mutiplier2(.clock(clk), .aclr(async), .dataa(r_reg3_1), .datab(r_reg3_2), .result(r_temp2)); // (a4*x + a3)*x
//normmul multiplier2(.dataa(r_reg3_1), .datab(r_reg3_2), .result(r_temp2));
assign r_next3 = r_temp2[29:12];

// Stage 4

adder add2(.clock(clk), .aclr(async), .dataa(r_reg4_2), .datab(coef2), .result(r_next4)); // ((a4*x + a3)*x + a2)
//normadd add2(.dataa(r_reg4_2), .datab(coef2), .result(r_next4));
// Stage 5

multiplier mutiplier3(.clock(clk), .aclr(async), .dataa(r_reg5_1), .datab(r_reg5_2), .result(r_temp3)); // ((a4*x + a3)*x + a2)*x
//normmul multiplier3(.dataa(r_reg5_1), .datab(r_reg5_2), .result(r_temp3));
assign r_next5 = r_temp3[29:12];

// Stage 6

adder add3(.clock(clk), .aclr(async), .dataa(r_reg6_2), .datab(coef1), .result(r_next6)); // (((a4*x + a3)*x + a2)*x + a1)
//normadd add3(.dataa(r_reg6_2), .datab(coef1), .result(r_next6));
// Stage 7

multiplier mutiplier4(.clock(clk), .aclr(async), .dataa(r_reg7_1), .datab(r_reg7_2), .result(r_temp4)); // (((a4*x + a3)*x + a2)*x + a1)*x
//normmul multiplier4(.dataa(r_reg7_1), .datab(r_reg7_2), .result(r_temp4));
assign r_next7 = r_temp4[29:12];

// Stage 8

adder add4(.clock(clk), .aclr(async), .dataa(r_reg8_1), .datab(coef0), .result(r_next8)); // (((a4*x + a3)*x + a2)*x + a1)*x + a0
//normadd add4(.dataa(r_reg8_1), .datab(coef0), .result(r_next8));


endmodule
