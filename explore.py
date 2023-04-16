
import dimod
from dimod.reference.samplers import ExactSolver
from dimod import drop_variables, quicksum
from dimod import BinaryQuadraticModel
from dimod.generators import and_gate, or_gate, xor_gate

def create_circuit(show=False):
    bqm_gate2 = or_gate("b", "c", "out2")
    bqm_gate3 = and_gate("a", "b", "out3")
    bqm_gate3.flip_variable("b")   # b -> (1-b)
    bqm_gate4 = or_gate("out2", "d", "out4")
    bqm_gate5 = and_gate("out3", "out4", "out5")
    bqm_gate7 = or_gate("out5", "out4", "z")
    bqm_gate7.flip_variable("out4")
    bqm = bqm_gate2 + bqm_gate3 + bqm_gate4 + bqm_gate5 + bqm_gate7

    if show:
        print(bqm.num_variables)
        print(bqm)

    return bqm


bqm = create_circuit()
sampleset_circuit = ExactSolver().sample(bqm).lowest(atol=0.2)