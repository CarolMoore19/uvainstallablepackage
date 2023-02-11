import sys
import pytest
sys.path.append('.')
import shared as sh


#Question 5:  Write Another Passing Test
# Make sure the function starts with `test_` and write any code that uses an assert.  
#Make sure the assert results in a `True` statement so it "passes". I.e.  `assert 1 == 1`.    
# (0.5 pt, although you'll get 1pt if the function runs your space compressor from the last function!)


def test_q5_space_compress_test_should_pass_one_point():
    sh.space_compress("This input for the      space compressor function is a string") 

#Q6.  Write a decorated failing test (use xfail)

@pytest.mark.xfail(reason="Test designed to fail.")
def test_q6_space_compress_test_should_fail():
    sh.space_compress(42)    

#Q7.  Add a test expected to fail, and skip it.

@pytest.mark.skip("Test skipped due to insufficient resources.")
def test_q7_skip_test():
    assert type("This is a string")==int

#Q8. Write a failing test and get it to skip only on your platform.

@pytest.mark.skipif(sys.platform=="darwin", reason= "Test skipped on my platform darwin")
def test_q8_skipif_onplatform():
    assert 1 == None

#Q9.  Set the wrong platform and watch the test execute.  It should fail.

@pytest.mark.skipif(sys.platform=="not_darwin", reason="Test skipped on other platforms")
def test_q9_skipif_other_platform():
    assert 1==None

#10.  Now add a `print("My platform is", sys.platform)` to the top of the test, before the assert.
# What happens when set up the conditions so the test runs and fails?  Do you see the printout?

@pytest.mark.skipif(sys.platform=="not_darwin", reason="Test skipped on other platforms")
def test_q10_skipif_other_print_platform():
    print("My platform is", sys.platform) 
    print("Yes, the print statement appears on the console.")
    assert 1==None
