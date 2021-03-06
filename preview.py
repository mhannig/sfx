#!/usr/bin/env python3

import sys
import time
import math

import pygame

import shaders

CHANNELS_ACTIVE=13

WIDTH = 300
HEIGHT = 800


SHADER = shaders.smooth_colors


def draw_strip(ctx, i, color):
    y = 20 + i * 50

    rect_up = (10, y, 280, 10)
    rect_dn = (10, y + 20, 280, 10)

    pygame.draw.rect(ctx, color, rect_up)
    pygame.draw.rect(ctx, color, rect_dn)


def _encode_rgbw(rgbw, bits):
    rgb = (min(rgbw[0] + rgbw[3], 1.0),
           min(rgbw[1] + rgbw[3], 1.0),
           min(rgbw[2] + rgbw[3], 1.0))

    return (round(rgb[0] * 255.0),
            round(rgb[1] * 255.0),
            round(rgb[2] * 255.0))


def render(ctx, t, proc):

    for i in range(0, CHANNELS_ACTIVE):
        # draw strip
        rgbw = proc(i, t)

        color = _encode_rgbw(rgbw, 8)
        draw_strip(ctx, i, color)


def main():
    pygame.init()

    display = pygame.display.set_mode((300, 800), 0, 32)

    t0 = time.time()

    while 42:
        # check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();

        t = time.time() - t0
        display.fill((0,0,0))
        render(display, t, SHADER)
        pygame.display.update()


if __name__ == "__main__":
    main()

