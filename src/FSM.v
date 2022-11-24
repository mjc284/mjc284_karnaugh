module FSM(
	 input clk,
	 input [1:0] in,
	 output [2:0] state
	);

	reg [2:0] reg_state = 3'b0;
	always @(posedge clk) begin
		reg_state[0] <= reg_state[1];
		reg_state[1] <= !reg_state[0]&!reg_state[1]&reg_state[3]&reg_state[4] | !reg_state[1]&reg_state[2];
		reg_state[2] <= !reg_state[0]&!reg_state[1]&!reg_state[2];
	end
endmodule