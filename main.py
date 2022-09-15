rows1 = int(input("number of rows on first page: "))
charsperrow1 = int(input("number of chars per row on first page: "))
rows2 = int(input("number of rows on second page: "))
charsperrow2 = int(input("number of chars per row on second page: "))

chars1 = rows1 * charsperrow1
chars2 = rows2 * charsperrow2

print(str(chars1) + " chars on first page,", str(chars2) + " chars on second page ")

final = [["      "]]

with open("zuowen.txt", "r") as f:
    data = f.readlines()

for para in data:
  for x in para:
    if "\n " in final[-1]:
      final[-1].remove("\n ")
    #four cases: numbers, punctuation, hanzi
    if x in "1234567890qwertyuiopasdfghjklzxcvbnm":
      final[-1][-1] = final[-1][-1] + x + " "
    elif x == "\n":
      pass
    else:
      final[-1][-1] = final[-1][-1] + x + " "
    #if last line in page has a length of charsperrow, start new line BUT with punctuation exceptions
    if len(final) % 2 == 0:
      if len(final[-1][-1]) >= charsperrow2*2:
        if final[-1][-1][0] in "。，、《》“”：（）":
          final[-1][-2] = final[-1][-2] + final[-1][-1][0] + " "
          final[-1][-1] = final[-1][-1][2:]
        elif final[-1][-1][0:6] == "      ":
          if len(final[-1][-1]) >= charsperrow2*2+2:
            final[-1].append("")     
        else:
          final[-1].append("")
    if len(final) % 2 == 1:
      if len(final[-1][-1]) >= charsperrow1*2:
        if final[-1][-1][0] in "。，、《》“”：（）":
          final[-1][-2] = final[-1][-2] + final[-1][-1][0] + " "
          final[-1][-1] = ""
        elif final[-1][-1][0:6] == "      ":
          if len(final[-1][-1]) >= charsperrow1*2+2:
            final[-1].append("")     
        else:
          final[-1].append("")
    #if page has a length of rows, start new page
    if len(final) % 2 == 0:
      if len(final[-1]) > rows2:
        final.append([""])
    if len(final) % 2 == 1:
      if len(final[-1]) > rows1:
        final.append([""])
  #new para, new line
  if len(final[-1][-1]) != 0:
    final[-1].append("      ")
  #if page has a length of rows, start new page
  if len(final) % 2 == 0:
    if len(final[-1]) > rows2:
      final.append([""])
      final[-2] = final[-2][:-2]
  if len(final) % 2 == 1:
    if len(final[-1]) > rows1:
      final.append([""])
      final[-2] = final[-2][:-2]

#printing
for page in range(len(final)):
  print("\npage " + str(page+1))
  header = "   "
  if page % 2 == 1:
    row = ""
    for y in range(charsperrow1):
      if y+1 < 10:
        header = header + "0" + str(y+1) + " "
      else:
        header = header + str(y+1) + " "
    print(header)
    for line in range(rows1):
      if line > len(final[page])-1:
        row = str(line+1) + ""
      elif line + 1 < 10:
        row = "0" + str(line+1) + " " + final[page][line]
      else:
        row = str(line+1) + " " + final[page][line]
      print(row)
  if page % 2 == 0:
    row = ""
    for y in range(charsperrow2):
      if y+1 < 10:
        header = header + "0" + str(y+1) + " "
      else:
        header = header + str(y+1) + " "
    print(header)
    for line in range(rows2):
      if line > len(final[page])-1:
        row = str(line+1) + ""
      elif line + 1 < 10:
        row = "0" + str(line+1) + " " + final[page][line]
      else:
        row = str(line+1) + " " + final[page][line]
      print(row)

#summary
print("\n")
pages = str(len(final)-1) + ""
lines = str(len(final[-1])-2) + ""
chars = str(len(final[-1][-2])/2) + ""
if len(final)-1 == 1:
  pages = pages + " page,"
else:
  pages = pages + " pages,"
if len(final[-1])-2 == 1:
  lines = lines + " line and"
else:
  lines = lines + " lines and"
if int(len(final[-1][-2])/2) == 1:
  chars = chars + " character"
else:
  chars = chars + " characters"
print("total length:", pages, lines, chars)

count = 0
for x in data:
  for y in "。，、《》“”：（）":
    x = x.replace(y, "")
  count += len(x)
print("total chinese characters:", str(count))

count = 0
for x in data:
  count += len(x)
print("total characters:", str(count) )

squares = 0
pages = len(final)
if len(final) % 2 == 0:
  squares = chars1 * (pages + 1) / 2 + chars2 * (pages - 1) / 2 + len(final[-1])-2 * charsperrow2 + len(final[-1][-2])/2
else:
  squares = chars1 * pages / 2 + chars2 * pages / 2 + len(final[-1])-2 * charsperrow1 + len(final[-1][-2])/2
  
print("squares occupied:", int(squares))
