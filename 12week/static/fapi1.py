from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO
import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

svae_path = 'qr_data.png'
qr_img.save(save_path)


@app.post("/qrcode/")
async def generate_qr(data: str = Form(...)):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4.
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black",back_color="white")
    
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()
    
    return StreamingResponse(BytesIO(img_byte_arr), media_type-"image/png")