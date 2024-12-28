import subprocess

def test_lesson_06():
    result = subprocess.run(['python3', 'lesson_06.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert "I am global" in output[0], f"Failed TODO 1: {output[0]}"
    assert "I am local" in output[1], f"Failed TODO 2: {output[1]}"
    assert "I am enclosing" in output[2], f"Failed TODO 3: {output[2]}"
    assert "Modified global" in output[3], f"Failed TODO 4: {output[3]}"
    assert "Modified enclosing" in output[4], f"Failed TODO 5: {output[4]}"
    assert "Local" in output[5] and "Global" in output[6], f"Failed TODO 6: {output[5]} {output[6]}"
    assert "4.0" in output[7], f"Failed TODO 7: {output[7]}"
    assert "debugged" in output[8], f"Failed TODO 8: {output[8]}"
    assert "nested value" in output[9], f"Failed TODO 9: {output[9]}"
    assert "LEGB order" in output[10], f"Failed TODO 10: {output[10]}"

    print("Lesson 6: All tests passed!")

if __name__ == "__main__":
    test_lesson_06()
