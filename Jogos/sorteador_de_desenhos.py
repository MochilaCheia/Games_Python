import random
from time import sleep

possiveis_desenhos = ['1- A rolling pin', '2- A hammock', '3- An anchor', '4- A skunk', '5- A desk chair',
                      '6- Van Gogh’s ear', '7- A sandwich', '8- A string quartet', '9- An ottoman',
                      '10- A bottle opener', '11- A fire escape', '12- Luminescent plankton', '13- A cabin',
                      '14- Mushrooms', '15- Shrubbery', '16- Bob Marley', '17- A full house', '18- Bubbles'
                      '19- Fangs', '20- A pickle', '21- An ironing board', '22- A dolphin', '23- A paper clip',
                      '24- A trumpet', '25- A burrito', '26- Tube socks', '27- A crayon', '28- A robot',
                      '29- A roller coaster', '30- A mosquito', '31- Fruit cocktail', '32- A peg leg',
                      '33- A spigot', '34- A balloon', '35- Head in the clouds', '36- The Milky Way',
                      '37- A knot', '38- An old key', '39- A submarine', '40- A tulip', '41- A gold medal',
                      '42- Synchronized swimmers', '43- Pom-poms', '44- A juice box', '45- A jar full of pennies',
                      '46- A bag of hammers', '47- Jelly beans', '48- A sundial', '49- A crystal ball',
                      '50- A synthesizer', '51- A paper airplane', '52- A water tower', '53- A surfboard',
                      '54- New Jersey', '55- Fiji', '56- A layer cake', '57- A panda', '58- A mime',
                      '59- Charlie Chaplin', '60- A penguin', '61- A seagull', '62- David Bowie',
                      '63- A sensitive cowboy', '64- A leopard', '65- An anatomy chart', '66- A tree limb',
                      '67- A ship in a bottle', '68- A mouth', '69- Brass knuckles', '70- An ear of corn',
                      '71- Costume jewelry', '72- A mirage', '73- Smoke', '74- Mold', '75- A rainbow',
                      '76- A dollar bill', '77- A bone',
                      '78- A glass of milk', '79- A teapot', '80- Weeds', '81- Dance steps',
                      '82- A turkey leg', '83- A pencil',
                      '84- A picket fence', '85- A Tiffany lamp', '86- The Empire State Building',
                      '87- A stalagmite', '88- A stalactite', '89- A kiss', '90- A ladybug', '91- A helmet',
                      '92- A paw print', '93- A Martian',
                      '94- A T-shirt', '95- A cinder block', '96- Swim fins', '97- A ripe banana',
                      '98- A barbell', '99- A tennis racket', '100- Japan', '101- A spiral staircase',
                      '102- A ponytail', '103- A campfire', '104- A squirrel', '105- A thumb', '106- A book',
                      '107- Girlish laughter', '108- Tangled ribbons', '109- Noodles', '110- Best friends',
                      '111- Worst enemies', '112- A lock', '113- An accordion', '114- A log',
                      '115- A melting candle', '116- A phone booth', '117- A geode', '118- Dice',
                      '119- Ointment', '120- A bucket', '121- A digital watch', '122- A bicycle',
                      '123- A cassette tape', '124- A library card', '125- A corn dog with mustard',
                      '126- Mittens', '127- A pocket', '128- A bunch of grapes', '129- A vending machine',
                      '130- A typewriter', '131- A flamingo', '132- A kebab', '133- Shelves', '134- A necklace',
                      '135- A dirty rag', '136- A scallion pancake', '137- A time machine',
                      '138- A Tyrannosaurus Rex', '139- A music box',
                      '140- A candelabra', '141- A quarter', '142- A bulldog', '143- A fairy',
                      '144- A ball of yarn', '145- A haircut', '146- An electric guitar', '147- Confetti',
                      '148- A pair of scissors', '149- A bandage', '150- A watermelon', '151- Bacon',
                      '152- A newsboy cap', '153- A seed pod', '154- A board game', '155- Daffodils',
                      '156- An onion', '157- A slinky', '158- A keychain', '159- A sand castle',
                      '160- Leftovers', '161- A ghost', '162- A vampire', '163- A football',
                      '164- A lightbulb', '165- A horseshoe', '166- A pug', '167- The Sunday paper',
                      '168- A helicopter', '169- A warthog', '170- A basket', '171- A skateboard',
                      '172- Sea spray', '173- Seaweed', '174- Hills and valleys', '175- An umbrella',
                      '176- A Christmas tree', '177- A hamburger', '178- Sunglasses', '179- A seal',
                      '180- Twenty thousand leagues under the sea', '181- A shooting star', '182- Handprints',
                      '183- A rotary phone', '184- A top hat', '185- A turtle', '186- A baseball', '187- Flags',
                      '188- An airplane', '189- A microphone', '190- A county fair', '191- A saxophone',
                      '192- An ice cream cone', '193- A marble', '194- A weathervane', '195- A lunchbox',
                      '196- A pound', '197- A trolley car', '198- Cat whiskers', '199- A cleaver',
                      '200- Electricity', '201- A Quonset hut', '202- A treasure chest', '203- Binoculars',
                      '204- A pumpkin', '205- A chalkboard', '206- Stiletto heels', '207- A crowd',
                      '208- A pile of tires', '209- A zombie', '210- French fries', '211- A butterfly',
                      '212- A watering can', '213- A cactus', '214- Coral', '215- Playing cars',
                      '216- A celebration', '217- A constellation', '218- The northern lights',
                      '219- Bonbons', '220- A wink', '221- An inchworm', '222- A knife',
                      '223- A kite', '224- The Olympics', '225- A box of tissues', '226- A balloon animal',
                      '227- A spiral-bound notebook', '228- A salt shaker', '229- A bearded lady',
                      '230- A wrinkle',
'A box of kittens',
'A slug',
'A shadow',
'A winter hat',
'A puzzle',
'A diving board',
'A spoon',
'A cuttlefish',
'Rain',
'Eyelashes',
'A unicorn',
'A diaper',
'A bottle cap',
'Queen Victoria',
'A bottle cap',
'A bird feeder',
'A baguette',
'A ladder',
'A parade',
'Running shoes',
'Bowling shoes',
'An apple tree',
'A storm',
'A fan',
'A princess crown',
'Broccoli',
'A sarcophagus',
'A stick of butter',
'A sled',
'A flattop',
'A tattoo',
'A bonnet',
'A baseball glove',
'Elvis',
'A rubber duck',
'A milk carton',
'A diamond ring',
'Feelings',
'Mom',
'Dad',
'A drunken sailor',
'A police officer',
'Snowshoes',
'A necktie',
'A bowler hat',
'A unicycle',
'A frog',
'A paper coffee cup',
'A circuit board',
'A waterslide',
'Spilled milk',
'Molten lava',
'A spaceship',
'A sound wave',
'Clogs',
'An open/closed sign',
'A view from an airplane window',
'Knitting needles',
'The Little Prince',
'A box of cereal',
'Toes',
'Chips and dip',
'A newt',
'A moustache',
'Cheese',
'A face full of character',
'An ugly duckling',
'A laser',
'The Leaning Tower of Pisa',
'Scrambled eggs',
'A caribou',
'An eyeball',
'A chimney',
'A drum kit',
'A battleship',
'Whirling dervishes',
'Building blocks',
'A fashion model',
'Fancy pants',
'Hot springs',
'Steak and potatoes',
'A spool of thread',
'The wild blue yonder',
'A rabbit',
'A boom box',
'A bird’s nest',
'A power tool',
'A butterfly',
'Toast',
'A computer',
'An eye patch',
'A crab apple',
'A golf ball',
'Cutlery',
'A Q-tip',
'Chocolate truffles',
'An office park',
'A sock monkey',
'A clock tower',
'A snorkel',
'A scorpion',
'A sardine tin',
'A secret door',
'A compound fracture',
'A bookstore',
'Dumplings',
'A prom dress',
'A bowl of pudding',
'A director’s chair',
'A beetle',
'A water jug',
'Your least favorite food',
'A turntable',
'A wheel of fortune',
'A fainting goat',
'A dumpster',
'A parasite',
'Lipstick',
'An oasis',
'A frying pan',
'Potato salad',
'Buttons',
'A lumberjack',
'An artichoke',
'A flower',
'A teacup',
'A map',
'A moose',
'A palm tree',
'A bear family',
'The Black forest',
'The periodic table',
'A keyboard',
'An anteater',
'A comet',
'A globe',
'Noah’s ark',
'Popcorn',
'Mac and cheese',
'The moon',
'An apron',
'An antelope',
'Petroleum jelly',
'An uneventful street',
'Bricks',
'A wormhole',
'A black hole',
'Perfume',
'A giraffe',
'A chainsaw',
'Cotton candy',
'A sidewalk',
'A sailboat',
'A fjord',
'A brain',
'Saturn',
'A ticket',
'A barrel of monkeys',
'A real estate agent',
'Tears',
'First love',
'Middle school',
'A lock',
'A tongue',
'Puget Sound',
'Peanut butter',
'A cranky old man',
'Roller skates',
'A pillow',
'A gnome',
'A bully',
'A puppet',
'An opera singer',
'Alphabet soup',
'A lollipop',
'Contrails',
'A hanger',
'A motel',
'A string of DNA',
'A squid',
'A stick of gum',
'A ballpoint pen',
'A cornucopia',
'A gravestone',
'Teeth',
'Icicles',
'A snout',
'A cabbage patch',
'An inner tube',
'An elephant',
'An Egyptian pyramid',
'A narwhal',
'A swimming pool',
'Fresh air',
'An iceberg',
'A cello',
'A stoplight',
'Mistakes',
'A dream',
'A nightmare',
'A fire truck',
'A tea bag',
'Tiny ballerinas',
'An electrical outlet',
'A game-show host',
'A technological diagram',
'Footprints',
'A stain',
'Unmentionables',
'A porcupine',
'Alfred Hitchcock',
'Bugs',
'A thumbtack',
'A cupcake',
'A steak',
'A pirate flag',
'A bowling pin',
'A loading crane',
'A reflection',
'A jungle',
'A tube of toothpaste',
'A turnip',
'A trailer',
'An orb',
'A long-playing record',
'A centaur',
'Mount Rushmore',
'A labyrinth',
'Your pinky finger',
'A wooly mammoth',
'A boss',
'An ashtray',
'A walnut',
'A burlap sack',
'Mismatched earrings',
'Freckles',
'A swimsuit',
'A chessboard',
'A tetherball',
'Root beer',
'Dimples',
'A poodle',
'A box car',
'Donuts',
'A church',
'An architect',
'Nails',
'A cowbell',
'A bus stop',
'Leisure Wear',
'A huge gold frame',
'A whisper',
'A scream',
'A jellyfish',
'A skeleton',
'A toaster',
'A hummingbird',
'A condiment',
'A safety pin',
'A garden',
'Lucky charms',
'A partner in crime',
'The man in the moon',
'Platform shoes',
'A quilt',
'A doily',
'Vitamins',
'A belt buckle',
'A container ship',
'A scoundrel',
'Crutches',
'A dandy',
'A waterfall',
'A circus',
'A troll',
'A deserted island',
'An owl',
'A beaker',
'A jumper',
'A pearl',
'A broken toy',
'A seashell',
'A feathered hat',
'An amoeba',
'Tie-Dye',
'A bobsledder',
'A houseboat',
'A gourd',
'A saint',
'A playsuit',
'An orphan',
'A bow and arrow',
'A pinecone',
'Curtains',
'A chorus line',
'A wallet',
'A messenger bag',
'Shrimp cocktail',
'An eggbeater',
'A sheep',
'A blackberry bush',
'Spats',
'Dignity',
'A carrot top',
'A freezer',
'A Scottie dog',
'A pineapple upside-down cake',
'A telescope',
'A mystery box',
'A bird in the hand',
'A horse and carriage',
'Skee ball',
'A razor blade',
'A goldfish',
'A recycling bin',
'A palm reading',
'A road',
'Windows',
'An egg',
'A birdhouse',
'A sweatband',
'A strawberry',
'Sushi',
'A hippo',
'A prism',
'A sense of humor',
'Pie a la mode',
'A dragonfly',
'A tractor',
'A propaganda poster',
'Behind the scenes',
'2 x 4s',
'A lava lamp',
'A harmonica',
'A ruler',
'Virginia Woolf',
'A windmill',
'Plateaus',
'A crash-test dummy',
'A starfish',
'Rain boots',
'A shoulder shrug',
'A pomegranate',
'A certificate',
'A Beatles song',
'A hobo',
'A portal',
'A wheelbarrow',
'A three-toed sloth',
'A box of fried chicken',
'Wise babies',
'The Abominable Snow Man',
'Cookies',
'Prescription medication',
'Capes',
'A tarantula',
'A can of beans',
'A sand dollar',
'A bee',
'A parasol',
'An ink pot',
'A sippy cup',
'Maple syrup',
                      '594- A video game', '595- Tectonic plates', '596- A beach',
                      '597- A wedding dress', '598- A spelunker', '599- A calculator',
                      '600- A baby monster', '601- A transportation system',
                      '602- A swamp', '603- An invitation', '604- An oven', '605- A train',
                      '606- The Bermuda Triangle', '607- A heart', '608- A movie star',
                      '609- A spiderweb', '610- An igloo', '611- Presidential pets',
                      '612- Paisley', '613- A grandma', '614- Lightning',
                      '615- Wind', '616- Run-D.M.C.', '617- A tuxedo',
                      '618- A mayonnaise jar', '619- A lemon meringue pie',
                      '620- A sea urchin', '621- A canyon', '622- A cave', '623- A concert',
                      '624- A viper', '625- A phonograph', '626- A bow', '627- A convertible',
                      '628- Ski slopes', '629- A mummy', '630- Broken glass', '631- A bed',
                      '632- A bar of music', '633- Polka dots', '634- Woodgrain',
                      '635- Plaid', '636- Zigzag', '637- A tacky rug', '638- A plastic bag',
                      '639- A muffin tin', '640- A sweater', '641- A tuba', '642- Yourself']


def sorteio_aleatorio():
    print('Olá, eu sou sou Sorte! seu sorteador de desenhos!\n~Seja bem vindo!~\n')

    sleep(1)
    print('>> Para utilizar o sistema, basta responder a pergunta do jeito que preferir'
          ' e para encerrar basta responder não a pergunta.<<\n')

    sleep(1)
    print('Um arquivo de texto será criado para anotar quais desenhos você sortear, '
          'assim você não desenhará o mesmo por engano.\n')

    sorteio = input('Deseja sortear seu desenho?\n')
    print('As sugestões de desenhos foram retirados de "642 coisas para desenhar"')

    sleep(1)
    while sorteio != 'não':
        numeros_sortidos = random.choice(possiveis_desenhos)
        sleep(1)
        print(f'Você sorteou: {numeros_sortidos}. Divirta-se desenhando!\n')

        numero_itens = len(possiveis_desenhos)
        sleep(1)
        print(f'E o número de opções restantes é: {numero_itens}\n')

        possiveis_desenhos.remove(numeros_sortidos)

        sleep(1)
        sorteio = input('Deseja continuar sorteando?\n')


def sorterio_sequencia():
    print('Olá, eu sou sou Sorte! seu sorteador de desenhos!\n~Seja bem vindo!~\n')

    sleep(1)
    print('>> Para utilizar o sistema, basta responder a primeira e segunda perguntas com sim <<\n'
          '>> e depois do jeito que preferir para continuar <<\n'
          '>> e para encerrar basta responder não a alguma das perguntas.<<\n')

    sleep(1)
    print('Um arquivo de texto será criado para anotar quais desenhos você sortear, '
          'assim você não desenhará o mesmo por engano.\n')

    proxima = input('Vamos começar a sortear seus desenhos?\n')

    sleep(1)
    if proxima == 'sim':

        print('As sugestões de desenhos foram retirados de "642 coisas para desenhar"')
        sleep(1)

        for correr in possiveis_desenhos:
            confirmacao = input('Você gostaria de ver a sugestão?\n')

            sleep(1)
            if confirmacao == 'não':
                print('Tudo certo! te vejo na próxima vez!')
                break

            print(f'A sugestão é: {correr}, não se esqueça de se divirtir desenhando!')
            sleep(1)

    else:
        print('Tudo certo, até mais!')

if __name__=='__main__':
    #print(sorteio_aleatorio())
    print(sorterio_sequencia())
    pass


 # No arquivo de texto que for gerado pra adicionar os desenhos sorteados,
 # faça uma operação que conte os desenhos no arquivo de texto e subtraia menos 642.
 # Fazer a parte de criação de um arquivo de texto e o tratamento de erros no final quando acabam os itens da lista.