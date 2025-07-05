name =input("enter your name:")
print(f'''congratulations {name}.
      you are selcted for the job.
      date : 26:6:25''')

# a;ternative approach

a = '''dear <name>
       you are selected
        <date> '''
print(a.replace("<name>","virat").replace("<date>","26 september 2050"))
