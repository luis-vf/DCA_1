
module alu #(
    parameter DATA_WIDTH = 32,
    parameter CTRL_WIDTH = 5,
    parameter STATUS_WIDTH = 4,
    parameter SHAMT_WIDTH = 5,
    parameter DELAY = 0
)(
    input clk,
    input rst,
    input [DATA_WIDTH*2-1:0] dataIn,
    input [CTRL_WIDTH-1:0] ctrl,
    input [SHAMT_WIDTH-1:0] shamt,
    output [DATA_WIDTH-1:0] dataOut,
    output [STATUS_WIDTH-1:0] status
);

/**********
 *  Array Packing Defines
 **********/
//These are preprocessor defines similar to C/C++ preprocessor or VHDL functions
`define PACK_ARRAY(PK_WIDTH,PK_DEPTH,PK_SRC,PK_DEST, BLOCK_ID, GEN_VAR)    genvar GEN_VAR; generate for (GEN_VAR=0; GEN_VAR<(PK_DEPTH); GEN_VAR=GEN_VAR+1) begin: BLOCK_ID assign PK_DEST[((PK_WIDTH)*GEN_VAR+((PK_WIDTH)-1)):((PK_WIDTH)*GEN_VAR)] = PK_SRC[GEN_VAR][((PK_WIDTH)-1):0]; end endgenerate
`define UNPACK_ARRAY(PK_WIDTH,PK_DEPTH,PK_DEST,PK_SRC, BLOCK_ID, GEN_VAR)  genvar GEN_VAR; generate for (GEN_VAR=0; GEN_VAR<(PK_DEPTH); GEN_VAR=GEN_VAR+1) begin: BLOCK_ID assign PK_DEST[GEN_VAR][((PK_WIDTH)-1):0] = PK_SRC[((PK_WIDTH)*GEN_VAR+(PK_WIDTH-1)):((PK_WIDTH)*GEN_VAR)]; end endgenerate

wire [DATA_WIDTH -1:0]data[1:0];

`UNPACK_ARRAY(BIT_WIDTH,DEPTH,data,dataIn,U_BLK_0,idx_0)
/**********
 * Internal Signals
**********/

/**********
 * Glue Logic
 **********/
/**********
 * Synchronous Logic
 **********/
 always@(posedge clk)
/**********
 * Glue Logic
 **********/
/**********
 * Components
 **********/
/**********
 * Output Combinatorial Logic
 **********/

end module
