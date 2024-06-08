Formatting with pygments
========================

.. code-block:: sby
    :caption: example.sby

    # comments
    [options]
    mode bmc
    depth 200
    multiclock on

    [engines]
    smtbmc yices
    smtbmc bitwuzla
    abc bmc3

    [script]
    # this is parsed as yosys script
    read -formal top.sv

    [file top.sv]
    // this is parsed as systemverilog
    module top(...);
    ...
    endmodule

    [file defines.v]
    // this is parsed as verilog
    `define SOME_DEFINE

    [file defines.vhd]
    // this is parsed as vhdl
    entity top is
    ...
    end top;

    [files]
    more.sv
    source.sv
    files.sv
