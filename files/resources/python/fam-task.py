import pygame, csv, os, sys, random
from datetime import datetime

##########
# Appearances
##########

white = '#FFFFFF'
black = '#000000'
blue = '#0000FF'

input_file = 'pic-names.csv'
pic_dir = 'assets/'
results_dir = 'results/'

instructions = ['您将看到图片，以及图片所指代的名词', '请熟悉每张图片所指代的词', '按空格键进入下一张图片', '按回车键开始任务']

instruction_font = 'simsun'
instruction_font_size = 50
trial_font = 'simsun'
trial_font_size = 75

##########
# Functions
##########

# wipe screen
def wipe():
    pygame.draw.rect(screen, white, pygame.Rect(0, 0, screen_width, screen_height))
    pygame.display.flip()

# next trial
def next_trial():
    global pic, text, last_time, pic, text
    global subj, data, data_pic, data_label, trial_number
    wipe()
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    now_time = now.strftime("%H-%M-%S")
    current_time = pygame.time.get_ticks()
    if len(pics) > 0:
        # record data for last trial
        rt = current_time - last_time
        if trial_number != 0:
            data.append([now_date, now_time, subj, trial_number, data_pic, data_label, rt])
        # get a new random trial
        rand_key = random.choice(list(pics.keys()))
        # use screen proportion
        pic = pygame.transform.scale(pygame.image.load(pic_dir+rand_key),((screen_width*0.27),(screen_width*0.27)))
        text = text_font_trial.render(pics[rand_key], True, black)
        screen.blit(pic, ((screen_width*0.365),(screen_height*0.15)))
        screen.blit(text, text.get_rect(center = (screen_width*0.5, screen_height*0.75)))
        # change relevant variables
        data_pic = rand_key
        data_label = pics[rand_key]
        trial_number += 1
        pics.pop(rand_key)
        pygame.display.flip()
        last_time = pygame.time.get_ticks()
    else:
        # record data for last trial
        rt = current_time - last_time
        data.append([now_date, now_time, subj, trial_number, data_pic, data_label, rt])
        with open(results_dir+subj+'.csv', 'w', encoding='utf-8') as output:
            wr = csv.writer(output, lineterminator='\n')
            for row in data:
                wr.writerow(row)
        pygame.quit()
        sys.exit()

##########
# Main task
##########
def main():
    global screen, screen_width, screen_height, text_font_ins, text_font_trial
    global pics, pic, text, data, last_time, trial_number, subj
    # Set working directory to the location of this .py file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # create results folder if nonexistent
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # get a dict of pics and names with pics as keys and names as values
    with open(input_file, 'r', encoding='utf-8') as input:
        cr = csv.reader(input)
        content = [line for line in cr]
        pics = {}
        first = True
        for row in content:
            if first:
                first = False
            else:
                pics[row[1]] = row[0]

    # pygame initialisation
    pygame.init()
    # full screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # get screen size
    screen_width, screen_height = screen.get_size()
    clock = pygame.time.Clock()
    screen.fill(white)
    text_font_subj = pygame.font.SysFont('arial', 50)
    text_font_ins = pygame.font.SysFont(instruction_font, instruction_font_size)
    text_font_trial = pygame.font.SysFont(trial_font, trial_font_size)

    # manage double esc quit
    esc_pressed = False
    last_esc_time = 0
    double_esc_time = 500  # milliseconds

    # task variables
    subj = 's'
    data = [['date', 'time', 'subject', 'trial', 'pic', 'label', 'rt']]
    started = False
    entering_subject = True
    trial_number = 0
    pic = None
    text = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # quit if esc key is pressed twice within double_esc_time (500ms)
            elif event.type == pygame.KEYDOWN:
                # handle first half of quit if esc key pressed twice
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = True
                    current_time = pygame.time.get_ticks()
                    if esc_pressed and (current_time - last_esc_time) < double_esc_time:
                        # write data file anyways even in case of force quit
                        with open(results_dir+subj+'.csv', 'w', encoding='utf-8') as output:
                            wr = csv.writer(output, lineterminator='\n')
                            for row in data:
                                wr.writerow(row)
                        pygame.quit()
                        sys.exit()
                    esc_pressed = True
                    last_esc_time = current_time
                ### handle subject number entering
                elif entering_subject:
                    if event.key == pygame.K_RETURN:
                        entering_subject = False
                        wipe()
                    elif event.key == pygame.K_BACKSPACE:
                        subj = subj[:-1]
                        wipe()
                    else:
                        subj += event.unicode
                        wipe()
                elif not started:
                    if event.key == pygame.K_RETURN:
                        started = True
                        last_time = pygame.time.get_ticks()
                        next_trial()
                else:
                    if event.key == pygame.K_SPACE:
                        next_trial()
            # second half of handling quit, when esc is up (unpressed), esc_pressed is set to false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = False
    
        if entering_subject:
            message1 = text_font_subj.render('Please enter subject number', True, black)
            screen.blit(message1, message1.get_rect(center = (screen_width*0.5, screen_height*0.3)))
            message2 = text_font_subj.render(subj, True, blue)
            screen.blit(message2, message2.get_rect(center = (screen_width*0.5, screen_height*0.5)))
            message3 = text_font_subj.render('Press Enter to continue', True, black)
            screen.blit(message3, message3.get_rect(center = (screen_width*0.5, screen_height*0.7)))
        elif not started:
            for i in range(len(instructions)):
                message = text_font_ins.render(instructions[i], True, black)
                screen.blit(message, message.get_rect(center = (screen_width*0.5, (i+1)*(screen_height*(1/(len(instructions)+1))))))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
