import logging
import csv
import argparse
import sys

logging.basicConfig(filename = "output.log", level = logging.DEBUG)

def put(name, snippet, filename):
    #Store a snippet with an associated name in the CSV file
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def make_parser():
  #Construct the command line parser
  logging.info("Constructing parser")
  description = "Store and retrieve snippets of text"
  parser = argparse.ArgumentParser(description = description)

  subparsers = parser.add_subparsers(dest="command", help="Available commnds")

  #subparser for the put command
  logging.debug("Constructing put subparser")
  put_parser = subparsers.add_parser("put", help = "Store a snippet")
  put_parser.add_argument("name", help = "The name of the snippet")
  put_parser.add_argument("snippet", help = "The snippet text")
  put_parser.add_argument("filename", default = "snippets.csv", nargs = "?", help = "The snippet filename")
<<<<<<< HEAD
  
  #subparser for the get command
  logging.debug("Constructing get subparser")
  get_parser = subparsers.add_parser('get', help="Get a snippet")
  get_parser.add_argument("name", help="The name of the snippet")
  get_parser.add_argument("filename", help="The snippet filename")
  
=======


>>>>>>> 25dbd3e4e6f9bc8200ec930aa9441c29b4d41f61
  return parser

def main():
  #Main function
  logging.info("Starting snippets")
  parser = make_parser()
  arguments = parser.parse_args(sys.argv[1:])
  #convert parsed arguments from namespace to dictionary
  arguments = vars(arguments)
  command = arguments.pop('command')

  if command == 'put':
    name, snippet = put(**arguments)
    print "Stored '{}' as '{}'".format(snippet, name)

if __name__ == "__main__":
  main()

