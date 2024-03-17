module denormalizer (input logic [17:0]x, output logic [17:0]y, input logic [3:0] Shift ,input logic LR);

always_comb begin
case(LR)
1'b0: y = x >> Shift;
1'b1: y = x << Shift;

endcase

end

endmodule
