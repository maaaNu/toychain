from toycoin.script_lang.interpreter import Interpreter
from toycoin.util import keypub_to_keypubhash

def test_script_1command_1constant():
    code = "OP_1\n1"
    inter = Interpreter.init(code)
    inter.execute()
    assert len(inter.stack) is 2

def test_unlocking_script():
    code = """304502207cd05e378a92e7c41198c698c7d54a387e495502a8cf2a8f214c748e22b090dd0221008980c14bc6b428d45d8735eed92da67e9f086d3e412d3dbbb2a50b2abdf729b5 
    3059301306072a8648ce3d020106082a8648ce3d03010703420004a469fee792b56101a51a1e98ec3e5f264e1293a03f8f18624da69ca9f19ed6abf3b24cd049d23aef3e42dbc27b5635654ee17552135c48c34972570e6a72f9ca 
    OP_DUP 
    OP_HASH160 
    0caf8c91f73362bd58adee5e58c74e4c3bb237b0 
    OP_EQUALVERIFY 
    OP_CHECKSIG
    """
    inter = Interpreter.init(code)
    print("code=" + str(inter.execution_code))
    inter.execute()
