# bowling.py

def score_game(rolls):
    """
    Calculates the total score of a single American Ten-Pin Bowling game.

    Parameters:
        rolls (list[int]): A list of integers representing the number of pins knocked down per roll.

    Returns:
        int: The total score of the game.
    """
    total_score = 0  # Final score to accumulate
    frame = 0  # Frame counter (10 frames total)
    i = 0  # Index to iterate through rolls

    for frame in range(10):
        if frame < 9:
            if rolls[i] == 10:
                # Strike: score is 10 + next two rolls
                total_score += 10 + rolls[i + 1] + rolls[i + 2]
                i += 1  # Move to next roll (frame only has one roll)
            elif rolls[i] + rolls[i + 1] == 10:
                # Spare: score is 10 + next roll
                total_score += 10 + rolls[i + 2]
                i += 2  # Move past two rolls of the current frame
            else:
                # Open frame: sum of two rolls
                total_score += rolls[i] + rolls[i + 1]
                i += 2  # Move past two rolls of the current frame
        else:
            if rolls[i] == 10:
                frame_sum = 10 + rolls[i + 1] + rolls[i + 2]
            else:
                if i + 1 < len(rolls) and rolls[i] + rolls[i + 1] == 10:
                      frame_sum = sum(rolls[i:i + 3])
                else:
                     frame_sum = sum(rolls[i:i + 2])
            total_score += frame_sum

    return total_score
