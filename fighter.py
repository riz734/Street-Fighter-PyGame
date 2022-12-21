import pygame

class Fighter():
    def __init__(self,x,y,flip,data,sprite_sheet,animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.running = False
        self.animation_list = self.load_images(sprite_sheet,animation_steps)
        self.flip = flip
        self.jump = False
        self.attack_type = 0
        self.attacking = False
        self.health = 100
        self.action = 0 #0>idle, 1>run,2>jump,3>attack1,4>attack2,5>hit,6>death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()

    def load_images(self,sprite_sheet,animation_steps):

        #extract images from spritesheet
        animation_list = []
        for y,animation in enumerate(animation_steps):
            temp_img_list = [] 
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                scaled_img = pygame.transform.scale(temp_img, (self.size * self.image_scale,self.size*self.image_scale))
                temp_img_list.append(scaled_img)
            #appends one row of images into animation list
            animation_list.append(temp_img_list)

        return animation_list

    def move(self,screen_width,screen_height,surface,target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.attack_type = 0

        #set to false when key is not pressed in next iter
        self.running = False
        #get keypresses
        key = pygame.key.get_pressed()

        #only when not attacking
        if self.attacking == False:
            #movement
            if key[pygame.K_a]:
                dx = -SPEED
                self.running = True
            if key[pygame.K_d]:
                dx = SPEED
                self.running = True
            #jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            
            #attack
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface,target)
                #which attack attack type
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2

        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y
        

        #detects screen borders, keeps player on screen
        if self.rect.left + dx < 0:
            dx =- self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - self.rect.bottom

        #make sure player facing each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True


        #update player position
        self.rect.x += dx
        self.rect.y += dy

    #handle updating animations
    def update(self):
        
        #which action player is performing
        #update_action(x), 0>idle,1>run,2>jump,3>attack1,4>attack2
        if self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3)
            elif self.attack_type ==2:
                self.update_action(4)

        elif self.jump == True:
            self.update_action(2)

        elif self.running == True:
            self.update_action(1)
        else:
            self.update_action(0)

        animation_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]
        #enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #check if animation is finished
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            #check if attack was used, if so then reset attack to false
            if self.action == 3 or self.action == 4:
                self.attacking = False


    def attack(self,surface,target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip),self.rect.y,2*self.rect.width,self.rect.height-10)
        if attacking_rect.colliderect(target.rect):
            print('hit')
            target.health -= 10
        pygame.draw.rect(surface,(0,255,0),attacking_rect)
        

    def update_action(self,new_action):
        #check if the new action is diff from current
        if new_action != self.action:
            self.action = new_action
            #update animation setting
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self,surface):
        img = pygame.transform.flip(self.image,self.flip,False)
        pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(img,(self.rect.x-(self.offset[0]*self.image_scale),self.rect.y-(self.offset[1]*self.image_scale)))