import math

def calculate_psnr(mse, max_pixel=255):
    if mse == 0:
        return float('inf')  # идеальное совпадение изображений
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

if __name__ == '__main__':
    # Используем ранее вычисленное значение MSE
    mse_value = 0.01
    psnr_value = calculate_psnr(mse_value)
    print(f'PSNR: {psnr_value} dB')

