from string import punctuation

Str = "Завари мне, пожалуйста, чай. Немедленно отойди от дороги!"
new_Str = ''

for i in Str:
    if i not in punctuation:
        new_Str = new_Str + i




print(new_Str)
