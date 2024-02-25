# script.py
import zipfile
import os

with open("code.py", encoding="utf-8") as code_file:
    your_code = code_file.read()

zip_name = list(filter(lambda x: x.endswith("zip"), os.listdir()))[0]

with zipfile.ZipFile(zip_name) as zip_file:

    tests_input = list(filter(lambda x: not x.endswith("clue"), zip_file.namelist()))
    tests_output = list(filter(lambda x: x.endswith("clue"), zip_file.namelist()))

    for input_file, out_file in zip(tests_input, tests_output):

        with zip_file.open(f"{input_file}") as file, zip_file.open(
            f"{out_file}"
        ) as clue_file:
            test_code = file.read().decode("utf-8")
            with open("test_script.py", "w", encoding="utf-8") as test_file:
                test_file.write(your_code + "\n" + test_code)

            answer = (
                os.popen("py test_script.py")
                .read()
                .strip()
                .replace('"', "")
                .replace("'", "")
            )
            clue = (
                clue_file.read()
                .decode("utf-8")
                .strip()
                .replace('"', "")
                .replace("'", "")
            )

            if answer.strip() == clue.strip():
                print(f"Test #{input_file} PASSED")
            else:
                print(f"Test #{input_file} DIDN'T PASSED")
                print(
                    f"""\nExpected this:\n{'-'*14}\n{clue}\n\nTaken this:\n{'-'*11}\n{answer}\n"""
                )
