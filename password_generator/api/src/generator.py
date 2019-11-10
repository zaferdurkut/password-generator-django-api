#!/usr/bin/env python3

import sys
import string
import random
import math
import os
import cv2
import numpy as np

def main(use_upper=True,
                use_lower=True,
                use_digits=True,
                use_punctuation=False,
                use_space=False,
                additional="",
                blacklist="",
                length=13,
                max_duplicate_chars=2):
    
    if not all(isinstance(x, bool) for x in
               [use_upper, use_lower, use_digits, use_punctuation, use_space]) \
            or not all(isinstance(x, str) for x in [additional, blacklist]):
        raise TypeError

    charset = make_charset(use_upper, use_lower, use_digits, use_punctuation, use_space,
                                 additional, blacklist)
                                 
    length = length
    max_duplicate_chars = max_duplicate_chars

    password = generate_password(charset, length, max_duplicate_chars)
    return password

def make_charset(use_upper, use_lower, use_digits, use_punctuation, use_space, additional, blacklist):
    if not all(isinstance(x, bool) for x in [use_upper, use_lower, use_digits, use_punctuation, use_space]) \
            or not all(isinstance(x, str) for x in [additional, blacklist]):
        raise TypeError

    return set(use_upper * string.ascii_uppercase +
               use_lower * string.ascii_lowercase +
               use_digits * string.digits +
               use_punctuation * string.punctuation +
               use_space * " " +
               additional) \
        .difference(set(blacklist))

def generate_password(charset, length, max_duplicate_chars):
    if not isinstance(charset, set) or not isinstance(length, int) or not isinstance(max_duplicate_chars, int):
        raise TypeError

    my_charset = charset.copy()
    password = ""
    while len(password) < length:
        password += random.SystemRandom().choice(list(my_charset))
        if max_duplicate_chars:
            for c in set(password):
                if password.count(c) >= max_duplicate_chars:
                    my_charset.discard(c)
    return password

def create_image(password,out_path="/app/password_generator/api/static/password.jpg"):
    length = len(password)*52
    # Write some Text
    img = np.ones((128,length,3), np.uint8)
    img = img *25
    shape=img.shape
    w=shape[1]
    h=shape[0]

    # Write some Text
    font                   = cv2.FONT_HERSHEY_COMPLEX
    bottomLeftCornerOfText = (int(w/10),int(h/2+20))
    fontScale              = 2
    fontColor              = (255,255,255)
    lineType               = 2
    cv2.putText(img,password, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)

    img = cv2.rectangle(img, (24,24), (length-24,int(h-24)), (141,13,13), 4)
    #Save image
    cv2.imwrite(out_path, img)
