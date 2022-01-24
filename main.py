import re
import argparse
import ntpath

html_base='''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Document</title>
    </head>
    <body>
'''
html_close='''</body>
</html>'''


RULES = {
    "### (?P<header>.*)?" : "<h3>\g<header></h3>",
    "## (?P<header>.*)?" : "<h2>\g<header></h2>",
    "# (?P<header>.*)?" : "<h1>\g<header></h1>",
    "\*\*(?P<bold>.*?)\*\*" : "<b>\g<bold></b>",
    "\*(?P<italic>.*?)\*" : "<i>\g<italic></i>",
    "~~(?P<deleted>.*?)~~" : "<del>\g<deleted></del>",
    "\[(?P<title>.*?)\]\((?P<link>.*?)\)" : '<a href="\g<link>">\g<title></a>',

    } 

def main():
    #parser that takes in file argument
    parse = argparse.ArgumentParser(description='Markdown to html parser')
    parse.add_argument('--file','-f',type=str,help='Path to the markdown file')
    args = parse.parse_args()

    #exit if file invalid
    if not args.file or not args.file.endswith('.md'):
        print("Invalid argument passed.Exiting...")
        return 
    
    try:
        with open(args.file) as file:
            doc = file.read()

        #substitute substrings using the RULES dictionary defined
        for key in RULES.keys():
            doc = re.sub(key,RULES[key],doc,re.M)

        output_path = ntpath.basename(args.file)
        with open(f'output/{output_path}.html','w')as output:
            output.write(html_base)
            output.write(doc)
            output.write(html_close)

        print('File converted successfully')
        return 
        
    except Exception as e:
        print(e)
        return

if __name__=='__main__':
    main()
    

    
    
   
