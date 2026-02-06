# User Input
landscape: str = input('Enter a landscape for the story: ')
animal: str = input('Enter an animal: ')
verb1: str = input('Enter a verb (for past tense): ')

verb2: str = input('Enter a verb (for past tense): ')

# Story

story: str = f'''
    A gust of wind shattered the stillness. Jack looked down to see the {landscape} unfold beyond his sight.
A place where the rumored {animal} made it's lair. He {verb1} off the cliff, rushing to the direction his soul-compass reached out,
when a sudden explosion discovered his legs. Jack {verb2} while he shot off to the air. The pain creeping into his spine, 
before a gust of wind shattered his consciousness.
'''

# Output

print('Result: ')
print(story)