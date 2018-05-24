# Main entry file for pyreduce.
import argparse

from master import execute_master

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--master', help='Execute the master node')
    parser.add_argument('--agent', help='Execute the Agent')
    parser.add_argument('--executor', help='Execute the job executor')
    args = parser.parse_args()

    if args.master:
        execute_master()
    elif args.agent:
        raise NotImplemented('Running an Agent is not yet implemented')
    elif args.executor:
        raise NotImplemented('Running an Executor is not yet implemented')

if __name__ == "__main__":
    main()