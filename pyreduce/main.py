# Main entry file for pyreduce.
import argparse

from master import execute_master
from agent import execute_agent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--master', dest='master', action='store_true',
                        help='Execute the master node')
    parser.add_argument('--agent', dest='agent', action='store_true', help='Execute the Agent')
    parser.add_argument('--executor', dest='executor', action='store_true',
                        help='Execute the job executor')
    args = parser.parse_args()

    if args.master:
        execute_master()
    elif args.agent:
        execute_agent()
    elif args.executor:
        raise NotImplemented('Running an Executor is not yet implemented')


if __name__ == "__main__":
    main()