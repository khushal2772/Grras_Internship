import argparse

paser = argparse.ArgumentParser(description= "Simple Calculator")

paser.add_argument('num1',type = float, help="first no.")
paser.add_argument('num2',type = float, help="second no.")
paser.add_argument('operation', choices=['add','sub','div','mul'])

args = paser.parse_args()

if args.operation == 'add':
    print(f'the result is {args.num1+args.num2}')