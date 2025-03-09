import multiprocessing
import subprocess
import time

def run_project():

    # Run the Python file containing your project code
    subprocess.run(["python", "generate_algerian_facebook_account.py"])

if __name__ == '__main__':
    num_processes = 5 # Set the number of processes you want to run concurrently

    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=run_project)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
