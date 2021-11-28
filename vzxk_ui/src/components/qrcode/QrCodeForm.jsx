import React,{useState, useEffect} from "react";
import axios from "axios";
import FormButton from "../ui/FormButton/FormButton";
import FormInput from "../ui/input/FormInput";

export default function QrCodeForm() {

    const [qrcode, setQrCode] = useState('')

    async function fetchPostQrCode() {
        axios.post('http://127.0.0.1:8000/qrcode/',
        {
            code: qrcode
        })
        setQrCode('')
    }

    return (
        <div>
            <FormInput
                value = {qrcode}
                placeholder = 'Штрих-код'
                type = 'text'
                onChange={e => setQrCode(e.target.value)}
                />
            <FormButton onClick={fetchPostQrCode}>Добавить</FormButton>
        </div>
    )

}

