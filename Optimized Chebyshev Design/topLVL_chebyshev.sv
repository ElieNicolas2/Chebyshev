module topLVL_chebyshev(input logic CLOCK_50, input logic [0:0] KEY, output logic [12:0] DRAM_ADDR, output logic [1:0] DRAM_BA,
output logic DRAM_CAS_N, output logic DRAM_CKE, output logic DRAM_CLK, output logic DRAM_CS_N, 
inout logic [15:0] DRAM_DQ, output logic DRAM_LDQM, output logic DRAM_UDQM, output logic DRAM_WE_N, output logic DRAM_RAS_N);

logic [17:0] xx_int, xy_int, y_int; 

ChebyshevTop insty (.x(xx_int), .xy(xy_int), .clk(CLOCK_50), .async(1'b0), .yfinal(y_int));

	Cheby u0 (
		.clk_clk                          (CLOCK_50),                          //clk.clk
		.reset_reset_n                    (1'b1),                   	        //reset.reset_n
		.pll_0_sdram_clk                  (DRAM_CLK),                  	     //pll_0_sdram.clk
		.sdram_controller_0_wire_addr     (DRAM_ADDR),     		              //sdram_controller_0_wire.addr
		.sdram_controller_0_wire_ba       (DRAM_BA),                           //.ba
		.sdram_controller_0_wire_cas_n    (DRAM_CAS_N),                        //.cas_n
		.sdram_controller_0_wire_cke      (DRAM_CKE),                          //.cke
		.sdram_controller_0_wire_cs_n     (DRAM_CS_N),                         //.cs_n
		.sdram_controller_0_wire_dq       (DRAM_DQ),                           //.dq
		.sdram_controller_0_wire_dqm      ({DRAM_UDQM, DRAM_LDQM}),            //.dqm
		.sdram_controller_0_wire_ras_n    (DRAM_RAS_N),                        //.ras_n
		.sdram_controller_0_wire_we_n     (DRAM_WE_N),     		              //.we_n
		.inputx_external_connection_export      (xx_int),                      //inputx_external_connection.export
		.inputy_external_connection_export      (xy_int),                      //inputy_external_connection.export
		.finaloutput_external_connection_export (y_int)                        //finaloutput_external_connection.export
	);


endmodule	
	
	
	
	
	
	
	


