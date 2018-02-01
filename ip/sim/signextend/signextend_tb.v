module signextend_tb();

parameter DATA_WIDTH_IN = 16;
parameter DEPTH = 4;
parameter DATA_WIDTH_OUT = 32;

`define DELAY(TIME_CLK) #(10*TIME_CLK);

reg clk = 0;
reg simState = 0;
reg [DATA_WIDTH_IN*DEPTH-1:0]dataIn;
wire [DATA_WIDTH_OUT*DEPTH-1:0]dataOut;

always begin
    if (simState != 1) begin
      `DELAY(1/2)
      clk = ~clk;
    end
end

initial begin
    $monitor("Data In is: %h    Data Out is: %h ",dataIn,dataOut);
    dataIn <= 64'hF0007000F0007000;
    `DELAY(5)
    dataIn <= 64'h7000F0007000F000;
    `DELAY(5)
    $stop;
end

signextend #(
    .DATA_WIDTH_IN(DATA_WIDTH_IN),
    .DEPTH(DEPTH),
    .DATA_WIDTH_OUT(DATA_WIDTH_OUT)
    )UUT(
    .dataIn(dataIn),
    .dataOut(dataOut)
);

endmodule // signextend_tb
