import React from 'react';
import bot from '../img/bot.png';
import you from '../img/user.png';

export default function Message({ message }) {
    const { content, sender, timestamp } = message;

    const messageClasses = sender === 'user' ? 'bg-blue' : 'bg-[#00df9a]';
    const alignmentClasses = sender === 'user' ? 'ml-auto' : 'mr-auto';
    const iconClasses = sender === 'user' ? you : bot ;

    return (
        <div className={`px-10 py-5 ${alignmentClasses}`}>
            <div className={` text-white p-3 rounded border flex ${messageClasses} `}>
                <div className='w-10'>
                    <img src={iconClasses} alt="Icon" className=''></img>
                </div>
                <div className=''>
                    <p>{content}</p>
                    <p className="text-sm bottom-1 right-1">{timestamp}</p>
                </div>
            </div>
        </div>
    );
}
