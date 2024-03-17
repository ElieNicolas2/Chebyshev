module topCheby(input logic clock, rst, 
					 input logic [17:0] x, output logic [17:0] y);

logic [17:0] cnst0, cnst1, cnst2, cnst3, cnst4;
logic outOfRange;
				 
always_comb begin
					 
if(x >= -6 && x < -5)begin

cnst0 = 18'H0161D;
cnst1 = 18'H00C67;
cnst2 = 18'H002B3;
cnst3 = 18'H00044;
cnst4 = 18'H00003;
outOfRange = 1'b0;

end

if(x >= -5 && x < -4)begin

cnst0 = 18'H01EDC;
cnst1 = 18'H0136F;
cnst2 = 18'H004D3;
cnst3 = 18'H0008E;
cnst4 = 18'H00006;
outOfRange = 1'b0;

end 

else if(x >= -4 && x < -3)begin

cnst0 = 18'H0249A;
cnst1 = 18'H01920;
cnst2 = 18'H006F1;
cnst3 = 18'H000E8;
cnst4 = 18'H0000B;
outOfRange = 1'b0;

end 

else if(x >= -3 && x < -2)begin

cnst0 = 18'H02388;
cnst1 = 18'H0276F;
cnst2 = 18'H005F6;
cnst3 = 18'H000A7;
cnst4 = 18'H00006;
outOfRange = 1'b0;

end 

else if(x >= -2 && x < -1)begin

cnst0 = 18'H0204E;
cnst1 = 18'H010F2;
cnst2 = 18'H00101;
cnst3 = 18'HFFEF3;
cnst4 = 18'HFFFCD;
outOfRange = 1'b0;

end 

else if(x >= -1 && x < 0)begin

cnst0 = 18'H02000;
cnst1 = 18'H00FFE;
cnst2 = 18'HFFFED;
cnst3 = 18'HFFE75;
cnst4 = 18'HFFFBB;
outOfRange = 1'b0;

end

else if(x >= 0 && x < 1)begin

cnst0 = 18'H02000;
cnst1 = 18'H00FFE;
cnst2 = 18'H00023;
cnst3 = 18'HFFE75;
cnst4 = 18'H00044;
outOfRange = 1'b0;

end

else if(x >= 1 && x < 2)begin

cnst0 = 18'H01FB1;
cnst1 = 18'H010F2;
cnst2 = 18'HFFEFE;
cnst3 = 18'HFFEF3;
cnst4 = 18'H00032;
outOfRange = 1'b0;

end

else if(x >= 2 && x < 3)begin

cnst0 = 18'H01C77;
cnst1 = 18'H0176F;
cnst2 = 18'HFFA09;
cnst3 = 18'H000A7;
cnst4 = 18'HFFFF9;
outOfRange = 1'b0;
end

else if(x >= 3 && x < 4)begin

cnst0 = 18'H01B65;
cnst1 = 18'H01920;
cnst2 = 18'HFF90E;
cnst3 = 18'H000E8;
cnst4 = 18'HFFFF4;
outOfRange = 1'b0;

end

else if(x >= 4 && x < 5)begin

cnst0 = 18'H02123;
cnst1 = 18'H0136F;
cnst2 = 18'HFFB2C;
cnst3 = 18'H0008E;
cnst4 = 18'HFFFF9;
outOfRange = 1'b0;

end

else if(x >= 5 && x < 6)begin

cnst0 = 18'H029E4;
cnst1 = 18'H00C67;
cnst2 = 18'HFFD4C;
cnst3 = 18'H00044;
cnst4 = 18'HFFFFC;
outOfRange = 1'b0;

end

else if (x < -6) begin

cnst0 = 18'H00000;
cnst1 = 18'H00000;
cnst2 = 18'H00000;
cnst3 = 18'H00000;
cnst4 = 18'H00000;
outOfRange = 1'b1;

end
else if (x > 6) begin

cnst0 = 18'H01000;
cnst1 = 18'H00000;
cnst2 = 18'H00000;
cnst3 = 18'H00000;
cnst4 = 18'H00000;
outOfRange = 1'b1;

end

end

ChebyshevOptimized Cheby1 (.outOfRange(.F) ,.coef0(cnst0), .coef1(cnst1), .coef2(cnst2), .coef3(cnst3), .coef4(cnst4), .xin(x), .clk(clock), .async(rst), .yout(y));

endmodule
