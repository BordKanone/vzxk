import React from "react";
import FormInput from "./ui/input/FormInput";
import FormSelect from "./ui/selected/FormSelect";

export default function PostFilter({filter, setFilter}){
    return(
        <div>
            <FormInput
            value = {filter.query}
            onChange = {e => setFilter({...filter, query: e.target.value})}
            placeholder = 'Поиск' />
            <FormSelect
            value = {filter.sort}
            onChange = {selectedSort => setFilter({...filter, sort: selectedSort})}
            defaultValue='Сортировка' options={[
            {value: 'title', name:'По названию'},
            {value: 'body', name:'По содержанию'}
            ]}/>
        </div>
    )
}
