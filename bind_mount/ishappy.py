def isHappy(n):
    def getNextNumber(oldN):
        total = 0
        while oldN > 0:
            digit = oldN % 10
            total += digit * digit
            oldN //= 10
        return total

    seen = []
    while n != 1:
        if n in seen:
            return False
        seen.append(n)
        n = getNextNumber(n)
    return True


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")
