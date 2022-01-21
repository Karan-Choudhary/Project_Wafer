import os
import argparse
import yaml
import logging





if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", help="Path to config file",default="default")
    args.add_argument("--datasource", help="Path to datasource",default=None)

    parsed_args = args.parse_args()
    print(parsed_args)