from projectq import MainEngine
from projectq.ops import H, Rx, X, Measure
from projectq.meta import Control,Dagger,Loop
from projectq.backends import CircuitDrawer

def RX_C(qubit, c):  #用函数包装
    Rx(c) | qubit
    H | qubit

drawing_engine = CircuitDrawer()
eng = MainEngine(drawing_engine)
qubit1 = eng.allocate_qubit()
qubit2 = eng.allocate_qubit()


RX_C(qubit1, 2) # apply a Hadamard gate
with Control(eng, qubit1):  #meta.Control实现控制门
    H | qubit2

with Dagger(eng):  #meta.Dagger实现完整代码块的反转
    H | qubit1

with Loop(eng ,2):  #meta.Loop实现循环
    H | qubit1
    X | qubit1


Measure | qubit1  # measure the qubit1
Measure | qubit2  # measure the qubit2
eng.flush()  # flush all gates (and execute measurements)
print("Measured {}".format(int(qubit1)))
print("Measured {}".format(int(qubit2)))
print(drawing_engine.get_latex()) #输出电路图latex代码