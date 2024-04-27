"""This example spawns (bouncing) balls randomly on a L-shape constructed of 
two segment shapes. Not interactive.
"""

__docformat__ = "reStructuredText"

# Python imports
import random
from typing import List

# Library imports
import pygame

# pymunk imports
import pymunk
import pymunk.pygame_util

MAX_BALLS = 2

class BouncyBalls(object):
    """
    This class implements a simple scene in which there is a static platform (made up of a couple of lines)
    that don't move. Balls appear occasionally and drop onto the platform. They bounce around.
    """

    def __init__(self) -> None:
        # Space
        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)

        # Physics
        # Time step
        self._dt = 1.0 / 60.0
        # Number of physics steps per screen frame
        self._physics_steps_per_frame = 1

        # pygame
        pygame.init()
        self._screen = pygame.display.set_mode((400, 400))
        self._clock = pygame.time.Clock()

        self._draw_options = pymunk.pygame_util.DrawOptions(self._screen)

        # Static barrier walls (lines) that the balls bounce off of
        self._add_static_scenery()

        # Balls that exist in the world
        self._balls: List[pymunk.Circle] = []

        # Execution control and time until the next ball spawns
        self._running = True
        self._ticks_to_next_ball = 10

    def run(self) -> None:
        """
        The main loop of the game.
        :return: None
        """

        # Main loop
        while self._running:
            # Progress time forward
            for x in range(self._physics_steps_per_frame):
                self._space.step(self._dt)

            self._process_events()
            
            self._update_balls()
                
            self._clear_screen()
            self._draw_objects()
            pygame.display.flip()
            # Delay fixed time between frames
            self._clock.tick(50)
            pygame.display.set_caption("fps: " + str(self._clock.get_fps()))

    def _add_static_scenery(self) -> None:
        """
        Create the static bodies.
        :return: None
        """
        static_body = self._space.static_body
        static_lines = [
            pymunk.Segment(static_body, (100, 100), (300, 100), 0.0),  # Top side
            pymunk.Segment(static_body, (300, 100), (300, 300), 0.0),  # Right side
            pymunk.Segment(static_body, (300, 300), (100, 300), 0.0),  # Bottom side
            pymunk.Segment(static_body, (100, 300), (100, 100), 0.0),  # Left side
        ]
        for line in static_lines:
            line.elasticity = 1.0
            line.friction = 0.0
        self._space.add(*static_lines)

    def _process_events(self) -> None:
        """
        Handle game and events like keyboard input. Call once per frame only.
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.image.save(self._screen, "bouncing_balls.png")

    def _update_balls(self) -> None:
        """
        Create/remove balls as necessary. Call once per frame only.
        :return: None
        """
        
        self._ticks_to_next_ball -= 1
        
        if self._ticks_to_next_ball <= 0:
            self._create_ball()
            self._ticks_to_next_ball = 100
        
        # Remove balls that fall below 100 vertically
        balls_to_remove = [ball for ball in self._balls if ball.body.position.y > 500]
        for ball in balls_to_remove:
            self._space.remove(ball, ball.body)
            self._balls.remove(ball)

    def _create_ball(self) -> None:
        """
        Create a ball.
        :return:
        """
        mass = 10
        radius = 25
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        
        body.position = 200, 200
        
         # Set initial velocity here
        initial_velocity = (0, 100)
        body.velocity = initial_velocity
        
        shape = pymunk.Circle(body, radius, (0, 0))
        shape.elasticity = 1.0
        shape.friction = 0.0
        self._space.add(body, shape)
        self._balls.append(shape)

    def _clear_screen(self) -> None:
        """
        Clears the screen.
        :return: None
        """
        self._screen.fill(pygame.Color("white"))

    def _draw_objects(self) -> None:
        """
        Draw the objects.
        :return: None
        """
        self._space.debug_draw(self._draw_options)
        
        font = pygame.font.Font(None, 20)
        
        for ball in self._balls:
            velocity_text = font.render(f"Velocity: {ball.body.velocity}", True, pygame.Color("black"))
            self._screen.blit(velocity_text, (ball.body.position.x - 40, ball.body.position.y + 30))


def main():
    game = BouncyBalls()
    game.run()


if __name__ == "__main__":
    main()