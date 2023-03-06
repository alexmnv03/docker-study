import fs from 'fs'

fs.appendFile('my-file.txt', 'Файл создан', (err) => {
    if (err) throw err
        console.log('Файл сохранен!')
})

setTimeout(() => console.log('Timeout - end'), 30000)
