const connectToDatabase = () => {
    const dummyPromise = new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("Connected to database");
            resolve();
        }, 1000);
    });
    return dummyPromise;
}

export default connectToDatabase;