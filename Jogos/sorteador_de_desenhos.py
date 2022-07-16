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
                      '76- A dollar bill', '77- A bone', '78- A glass of milk', '79- A teapot', '80- Weeds',
                      '81- Dance steps', '82- A turkey leg', '83- A pencil', '84- A picket fence',
                      '85- A Tiffany lamp', '86- The Empire State Building',
                      '87- A stalagmite', '88- A stalactite', '89- A kiss', '90- A ladybug', '91- A helmet',
                      '92- A paw print', '93- A Martian', '94- A T-shirt', '95- A cinder block',
                      '96- Swim fins', '97- A ripe banana', '98- A barbell', '99- A tennis racket',
                      '100- Japan', '101- A spiral staircase', '102- A ponytail', '103- A campfire',
                      '104- A squirrel', '105- A thumb', '106- A book',
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
                      '230- A wrinkle', '231- A box of kittens', '232- A slug', '233- A shadow',
                      '234- A winter hat', '235- A puzzle', '236- A diving board', '237- A spoon',
                      '238- A cuttlefish', '239- Rain', '240- Eyelashes', '241- A unicorn',
                      '242- A diaper', '243- A bottle cap', '244- Queen Victoria',
                      '245- A bottle cap', '246- A bird feeder', '247- A baguette', '248- A ladder',
                      '249- A parade', '250- Running shoes', '251- Bowling shoes', '252- An apple tree',
                      '253- A storm', '254- A fan', '255- A princess crown', '256- Broccoli',
                      '257- A sarcophagus', '258- A stick of butter', '259- A sled', '260- A flattop',
                      '261- A tattoo', '262- A bonnet', '263- A baseball glove', '264- Elvis',
                      '265- A rubber duck', '266- A milk carton', '267- A diamond ring',
                      '268- Feelings', '269- Mom', '270- Dad', '271- A drunken sailor',
                      '272- A police officer', '273- Snowshoes', '274- A necktie', '275- A bowler hat',
                      '276- A unicycle', '277- A frog', '278- A paper coffee cup', '279- A circuit board',
                      '280- A waterslide', '281- Spilled milk', '282- Molten lava', '283- A spaceship',
                      '284- A sound wave', '285- Clogs', '286- An open/closed sign',
                      '287- A view from an airplane window', '288- Knitting needles', '289- The Little Prince',
                      '290- A box of cereal', '291- Toes', '292- Chips and dip', '293- A newt',
                      '294- A moustache', '295- Cheese', '296- A face full of character',
                      '297- An ugly duckling', '298- A laser', '299- The Leaning Tower of Pisa',
                      '300- Scrambled eggs', '301- A caribou', '302- An eyeball', '303- A chimney',
                      '304- A drum kit', '305- A battleship', '306- Whirling dervishes', '307- Building blocks',
                      '308- A fashion model', '309- Fancy pants', '310- Hot springs', '311- Steak and potatoes',
                      '312- A spool of thread', '313- The wild blue yonder', '314- A rabbit', '315- A boom box',
                      '316- A bird’s nest', '317- A power tool', '318- A butterfly', '319- Toast',
                      '320- A computer', '321- An eye patch', '322- A crab apple', '323- A golf ball',
                      '324- Cutlery', '325- A Q-tip', '326- Chocolate truffles', '327- An office park',
                      '328- A sock monkey', '329- A clock tower', '330- A snorkel', '331- A scorpion',
                      '332- A sardine tin', '333- A secret door', '334- A compound fracture',
                      '335- A bookstore', '336- Dumplings', '337- A prom dress', '338- A bowl of pudding',
                      '339- A director’s chair', '340- A beetle', '341- A water jug',
                      '342- Your least favorite food', '343- A turntable', '344- A wheel of fortune',
                      '345- A fainting goat', '346- A dumpster', '347- A parasite', '348- Lipstick',
                      '349- An oasis', '350- A frying pan', '351- Potato salad', '352- Buttons',
                      '353- A lumberjack', '354- An artichoke', '355- A flower', '356- A teacup',
                      '357- A map', '358- A moose', '359- A palm tree', '360- A bear family',
                      '361- The Black forest', '362- the periodic table', '363- A keyboard',
                      '364- An anteater', '365- A comet', '366- A globe', '367- Noah’s ark',
                      '368- Popcorn', '369- Mac and cheese', '370- The moon', '371- An apron',
                      '372- An antelope', '373- Petroleum jelly', '374- An uneventful street',
                      '375- Bricks', '376- A wormhole', '377- A black hole', '378- Perfume',
                      '379- A giraffe', '380- A chainsaw', '381- Cotton candy', '382- A sidewalk',
                      '383- A sailboat', '384- A fjord', '385- A brain', '386- Saturn', '387- A ticket',
                      '388- A barrel of monkeys', '389- A real estate agent', '390- Tears', '391- First love',
                      '392- Middle school', '393- A lock', '394- A tongue', '395- Puget Sound',
                      '396- Peanut butter', '397- A cranky old man', '398- Roller skates', '399- A pillow',
                      '400- A gnome', '401- A bully', '402- A puppet', '403- An opera singer',
                      '404- Alphabet soup', '405- A lollipop', '406- Contrails', '407- A hanger',
                      '408- A motel', '409- A string of DNA', '410- A squid', '411- A stick of gum',
                      '412- A ballpoint pen', '413- A cornucopia', '414- A gravestone', '415- Teeth',
                      '416- Icicles', '417- A snout', '418- A cabbage patch', '419- An inner tube',
                      '420- An elephant', '421- An Egyptian pyramid', '422- A narwhal',
                      '423- A swimming pool', '424- Fresh air', '425- An iceberg', '426- A cello',
                      '427- A stoplight', '428- Mistakes', '429- A dream', '430- A nightmare',
                      '431- A fire truck', '432- A tea bag', '433- Tiny ballerinas', '434- An electrical outlet',
                      '435- A game-show host', '436- A technological diagram', '437- Footprints',
                      '438- A stain', '439- Unmentionables', '440- A porcupine', '441- Alfred Hitchcock',
                      '442- Bugs', '443- A thumbtack', '444- A cupcake', '445- A steak', '446- A pirate flag',
                      '447- A bowling pin', '448- A loading crane', '449- A reflection', '450- A jungle',
                      '451- A tube of toothpaste', '452- A turnip', '453- A trailer', '454- An orb',
                      '455- A long-playing record', '456- A centaur', '457- Mount Rushmore', '458- A labyrinth',
                      '459- Your pinky finger', '460- A wooly mammoth', '461- A boss', '462- An ashtray',
                      '463- A walnut', '464- A burlap sack', '465- Mismatched earrings', '466- Freckles',
                      '467- A swimsuit', '468- A chessboard', '469- A tetherball', '470- Root beer',
                      '471- Dimples', '472- A poodle', '473- A box car', '474- Donuts', '475- A church',
                      '476- An architect', '478- Nails', '479- A cowbell', '480- A bus stop',
                      '481- Leisure Wear', '482- A huge gold frame', '482- A whisper', '483- A scream',
                      '484- A jellyfish', '485- A skeleton', '486- A toaster', '487- A hummingbird',
                      '488- A condiment', '489- A safety pin', '490- A garden', '491- Lucky charms',
                      '492- A partner in crime', '493- The man in the moon', '494- Platform shoes', '495- A quilt',
                      '496- A doily', '497- Vitamins', '498- A belt buckle', '499- A container ship',
                      '500- A scoundrel', '501- Crutches', '502- A dandy', '503- A waterfall', '504- A circus',
                      '505- A troll', '506- A deserted island', '507- An owl', '508- A beaker', '509- A jumper',
                      '510- A pearl', '511- A broken toy', '512- A seashell', '513- A feathered hat',
                      '514- An amoeba', '515- Tie-Dye', '516- A bobsledder', '517- A houseboat', '518- A gourd',
                      '519- A saint', '520- A playsuit', '521- An orphan', '522- A bow and arrow', '523- A pinecone',
                      '524- Curtains', '525- A chorus line', '526- A wallet', '527- A messenger bag',
                      '528- Shrimp cocktail', '529- An eggbeater', '530- A sheep', '531- A blackberry bush',
                      '532- Spats', '533- Dignity', '534- A carrot top', '535- A freezer', '536- A Scottie dog',
                      '537- A pineapple upside-down cake', '538- A telescope', '539- A mystery box',
                      '540- A bird in the hand', '541- A horse and carriage', '542- Skee ball',
                      '543- A razor blade', '544- A goldfish', '545- A recycling bin', '546- A palm reading',
                      '547- A road', '548- Windows', '549- An egg', '550- A birdhouse', '551- A sweatband',
                      '552- A strawberry', '553- Sushi', '554- A hippo', '555- A prism', '556- A sense of humor',
                      '557- Pie a la mode', '558- A dragonfly', '559- A tractor', '560- A propaganda poster',
                      '561- Behind the scenes', '562- 2 x 4s', '563- A lava lamp', '564- A harmonica',
                      '565- A ruler', '566- Virginia Woolf', '567- A windmill', '568- Plateaus',
                      '569- A crash-test dummy', '570- A starfish', '571- Rain boots', '572- A shoulder shrug',
                      '573- A pomegranate', '574- A certificate', '575- A Beatles song', '576- A hobo',
                      '577- A portal', '578- A wheelbarrow', '579- A three-toed sloth',
                      '580- A box of fried chicken', '581- Wise babies', '582- The Abominable Snow Man',
                      '583- Cookies', '584- Prescription medication', '585- Capes', '586- A tarantula',
                      '587- A can of beans', '588- A sand dollar', '589- A bee', '590- A parasol',
                      '591- An ink pot', '592- A sippy cup', '593- Maple syrup',
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

lista_usuario = []


def sorteador():
    print('Olá, eu sou sou Sorte! seu sorteador de desenhos!\n~Seja bem vindo!~\n')

    escolha = input('Primeiro, me diga qual lista de desenhos você gostaria de acessar: \n'
                    '1 - lista de 642 opções, 2 - Sua lista ou 3 - Criar nova lista\n'
                    'Basta digitar o número e apertar enter:\n')

    if escolha == '1':
        sleep(1)
        print('As sugestões de desenhos foram retirados de "642 coisas para desenhar"')
        modo = input('Você gostaria de receber os itens da lista aleatorimanete ou de maneira sequencial?\n'
                     'Digite -1- para aleatorio e -2- para sequencial:\n')

        if modo == '1':
            opcao = possiveis_desenhos
            sleep(1)
            print('>> Responda as perguntas como preferir e para encerrar digite -não- <<\n')
            sorteio = input('Deseja sortear seu desenho?\n')

            sleep(1)
            while sorteio != 'não':
                numeros_sortidos = random.choice(opcao)
                sleep(1)
                print(f'Você sorteou: {numeros_sortidos}. Divirta-se desenhando!\n')
                sleep(1)
                sorteio = input('Deseja continuar sorteando?\n')

        elif escolha == '2':
            sleep(1)
            print('As sugestões de desenhos foram retirados de "642 coisas para desenhar"')

            sleep(1)
            for correr in possiveis_desenhos:
                confirmacao = input('Quer uma sugestão de desenho?\n'
                                    '-sim- para continuar.')

                sleep(1)
                if confirmacao == 'sim':
                    print(f'A sugestão é: {correr}, não se esqueça de se divirtir desenhando!')
                    sleep(1)


if __name__ == '__main__':
    print(sorteador())

# No arquivo de texto gerado para adicionar os desenhos sorteados,
# faça uma operação que conte os desenhos no arquivo de texto e subtraia menos 642.
# Fazer a parte de criação de um arquivo de texto e o tratamento de erros no final quando acabam os itens da lista.
