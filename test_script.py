from unrollForeach_testing import unroll_call,cleanup
import os

cmd = "python unrollForeach_testing.py"
diff_cmd = "diff "
filename = "edge-editing-v2.tex"

os.system(cmd)


def test_snippets():
    for i in range(8):
        test_filename = "test_"+filename+"t"+str(i)+"_unrolled.txt"
        orig_filename = filename+"t"+str(i)+"_unrolled.txt"
        res = os.system("diff "+orig_filename+" "+test_filename)
        assert res == 512
        # os.system("rm "+ test_filename)
test_snippets()
cleanup()