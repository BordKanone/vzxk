import axios from 'axios';

export default class PostService{
    static async getAll() {
        try {
            const response = await axios.get('http://127.0.0.1:8000/customers/')
            return response.data
        } catch(e) {
            console.log('get posts')
            console.log(e)
        }
    }
}