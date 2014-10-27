# coding=UTF-8

from ui import *
import player

class TrainingGround:
  @staticmethod
  def run(current):
    ui.mes('Training Grounds Receptionist', ['Welcome! You are at the entrance of the ' + ui.green('Training Grounds') + '.', 'You\'re new to the Ragnarok world. Please choose your action:'])

    ans = ui.menu(current.name, ['Applying for Novice training.', 'Training Grounds Introduction.'])
    while ans == 1:
      ui.mes('Training Grounds Receptionist', ['This training grounds was established in order to provide useful information to new players of Ragnarok by the Rune-Midgarts Kingdom\'s Board of Education.', 'The training course is organized into two parts: the Basic Knowledge classes, and Field Combat training.', 'Through the first course, players will learn the necessary knowledge for a smoother gaming experience.', 'In Field Combat Training, players will engage in actual battle with weak monsters so they can learn the basics of fighting.', 'With this battle practice, players will be able to gain more experience before they enter the real world.', 'If you ready to participate in the training grounds, please choose ' + ui.green('Applying for Novice training') + ' in the menu.'])
      ans = ui.menu(current.name, ['Applying for Novice training.', 'Training Grounds Introduction.'])

    ui.mes('Training Grounds Receptionist', ['Thank you for applying for Novice training. For detailed information of each training course, please inquire the Guides for assistance.', 'You will now be transferred to the Training Grounds.'])

    ui.clear()

    while not current.has_npc(['Shion', 'Kris', 'Cecil']):
      ui.mes(current.name, ['There are some people in the ground, which do you want to chat with?'])

      ans = ui.menu(current.name, ['Shion', 'Kris', 'Cecil'])

      if ans == 0:
        if current.has_npc(['Shion']):
          ui.mes('Shion', ['I have nothing to teach you.', 'You should chat with Cecil.'])
        else:
          ui.mes('Shion', ['Hey, how are you?', 'I will tech you about player status.', 'Now let us open your status panel.'])

          ui.menu(current.name, ['Open status panel.'])

          current.status_panel()

          ui.mes('Shion', ['Lv means level, it will upgrade when your exp is full.', 'Hp is your health and you will die if your hp is zero.', 'Atk is your normal attack damage. Matk is your spell damage.', 'Str is strong, each point can increase max hp and atk.', 'Int is intelligence, each point can increase matk and probability cast.', 'Your str and int will increase randomly after you level up.'])

          ui.mes('Shion', 'Now I will increase your exp, then you can see your status panel.')

          ui.wait()

          current.add_exp(110)

          ui.mes('Shion', 'Do you feel better?')

          current.npcs['Shion'] = True

      if ans == 1:
        if current.has_npc(['Shion', 'Cecil']):
          ui.mes('Kris', 'Are you ready to fight?')
          ui.menu(current.name, ['Let\'s go!'])

          ui.clear()

          ans = 0
          while ans == 0:
            ui.mes(current.name, 'What do you want to do?')
            ans = ui.menu(current.name, ['Chat with Kris.', 'Attack Poring.'])
            if ans == 0:
              ui.mes('Kris', 'Try to attack Poring, you can do it.')

          current.attack_mob('Poring')

          ui.mes('Kris', ['Congratulations!', 'Now you can adventure by yourself.', 'I will transfer you to Prontera, the capital of the kingdom.'])

          current.npcs['Kris'] = True

          ui.wait()

          ui.clear()

          ui.mes('Kris', ['Oh, I forgot to archive your game data.', 'After archiving, you could load data when you play it next time.', 'Please reopen game after archiving completed.'])

          current.archive()

        else:
          ui.mes('Kris', 'Please chat with Shion and Cecil first.')

      if ans == 2:
        if current.has_npc(['Cecil']):
          ui.mes('Cecil', ['Greed is evil.', 'I have nothing to give you.'])
        else:
          ui.mes('Cecil', ['I\'m item teacher.', 'I will teach you about items.', 'There are 3 types items. They are ' + ui.green('Healings and Equipments') + '.', 'You can sell all of them to get money.', ui.green('Zeny') + ' is the unit of money.'])
          ui.mes('Cecil', 'Now I will give you some gifts.')

          ui.wait()
          current.add_item([['Knife', 1]])

          while not current.has_equiped('Knife'):
            ui.mes('Cecil', ['Now you can open your bag to see the gifts.', 'And try to ' + ui.green('equip Knife') + '.'])
            ui.menu(current.name, ['Open bag.'])
            current.bag_panel()

          ui.mes('Cecil', ['Good job!', 'Now you can open status panel to see weapon effect.'])
          ui.wait()
          current.status_panel()
          ui.mes('Cecil', ['The number after + is equipments\' effect.', 'Good equipments are important.'])

          current.npcs['Cecil'] = True
