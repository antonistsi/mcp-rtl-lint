module latch_example #() (
    input wire enable,
    input wire d,
    output reg q
);

    always_comb
    begin
        if (enable) begin
            q = d;
        end
        // Missing else branch causes a latch for q
    end
endmodule

