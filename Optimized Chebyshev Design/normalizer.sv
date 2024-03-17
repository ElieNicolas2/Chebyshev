module normalizer (input logic [17:0]x, output logic [17:0]y, output logic [3:0] Shift ,output logic LR);


logic[4:0] M;
logic[2:0] N;
logic K, C, G; 

always_comb begin
casex (x[11:0]) 
12'b1???????????: M = 5'b10000;

12'b01??????????: M = 5'b10001;

12'b001?????????: M = 5'b10010; 

12'b0001????????: M = 5'b10011;

12'b00001???????: M = 5'b10100;

12'b000001??????: M = 5'b10101;

12'b0000001?????: M = 5'b10110;

12'b00000001????: M = 5'b10111;

12'b000000001???: M = 5'b11000;

12'b0000000001??: M = 5'b11001;

12'b00000000001?: M = 5'b11010;

12'b000000000001: M = 5'b11011;
default : M = 5'b00000;
endcase


casex(x[17:12])

6'b1?????: N = 3'b101;

6'b01????: N = 3'b100;

6'b001???: N = 3'b011; 

6'b0001??: N = 3'b010;

6'b00001?: N = 3'b001;

6'b000001: N = 3'b000;
default : N = 3'b000;
endcase 

LR = x[17:12] ? 1'b1 : 1'b0;              // if LR 1, it means shift right, if 0 shift left.
K = M[4]? 1'b0: 1'b1;                     // if M[4] = 1, K = 0, else K = 1 which means that all 12 bits are 0's.

C = (x[17:12] == 6'b000001)? 1'b0 : 1'b1; // if equal 000001 C = 0, else C = 1.
G = C&K;
 
y = LR? x >> (N+ M[4] +G): x << M[3:0];
end 


assign Shift = LR ?(N + M[4]+G):M[3:0];

endmodule
