def puzzles(puzzleName):
    if puzzleName == "glassBridge":
        return """You are on a game show where you must cross a bridge made of 20 glass panels. 
        Some of these panels are strong enough to hold your weight, while others will shatter when stepped on. 
        You are given a single clue: the safe panels always align with Fibonacci numbers. 
        How do you safely cross the bridge?"""
    elif puzzleName == "lockedBox":
        return """You are locked in a room with a sealed box. The box has a combination lock with three digits. 
        Written on the wall is this riddle: 
        'The lock’s key lies within a prime number; divide it by 3, and the remainder is 2.' 
        What is the combination?"""
    elif puzzleName == "invisibleInk":
        return """A detective receives a blank letter in the mail. 
        Knowing it’s a clue, he places it under UV light, revealing a message: 
        'The truth is in the reflection of what you drink.' 
        What does the detective do to solve the case?"""
    elif puzzleName == "burningRope":
        return """You have two ropes and a lighter. Each rope burns unevenly but takes exactly 60 minutes to burn from one end to the other. 
        How can you measure exactly 45 minutes using these two ropes?"""
    else:
        return """Five people are trapped on an island and must cross a rickety bridge to escape. 
        The bridge can only hold two people at a time. They have one flashlight, and it must be carried whenever someone crosses the bridge. 
        Person A takes 1 minute to cross, B takes 2 minutes, C takes 5 minutes, D takes 10 minutes, and E takes 15 minutes. 
        How can they all cross the bridge in the shortest amount of time?"""
