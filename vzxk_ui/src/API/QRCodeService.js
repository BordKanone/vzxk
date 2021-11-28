import axios from 'axios';

export default class QRCodeService{
    static async getAll() {
        try {
            const response = await axios.get('http://127.0.0.1:8000/qrcode/')
            return response.data
        } catch(e) {
            console.log('get qr code ')
            console.log(e)
        }
    }
}