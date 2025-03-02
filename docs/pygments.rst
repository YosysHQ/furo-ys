Formatting with pygments
========================

.. code-block:: yoscrypt
   :caption: example.ys

   read_verilog fifo.v; :inline comments; prep -top fifo
   log "strings" # and comments
   ! echo "abc 123"; echo another # bash gets comments too

   label:     (unless -flag)
      log "now with labels"
      some_command [-option]      (-option if ___)
      select */t:SWITCH %x:+[GATE] */t:SWITCH %d

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

.. code-block:: sby
   :caption: pycode in sby

   [tasks]
   --pycode-begin--
   # pycode sections are python formatted
   for uut in "rotate reflect".split():
     for op in "SRL SRA SLL SRO SLO ROR ROL FSR FSL".split():
       output("%s_%s %s %s" % (uut, op, uut, op))
   --pycode-end--

   ...

   [script]
   --pycode-begin--
   for op in "SRL SRA SLL SRO SLO ROR ROL FSR FSL".split():
     if op in tags:
       output("read -define %s" % op)
   --pycode-end--
   rotate: read -define UUT=shifter_rotate
   reflect: read -define UUT=shifter_reflect
   read -sv test.v
   read -sv shifter_reflect.v
   read -sv shifter_rotate.v
   prep -top test

   ...


.. code-block:: sby
   :caption: tasks/tags in sby

   [tasks]
   task1 task_1_or_2 task_1_or_3
   task2 task_1_or_2
   task3 task_1_or_3

   task1 task2 : default

   [options]
   task_1_or_2:
   mode bmc
   depth 100

   task3:
   mode prove
   --
