export class RegistrationModel {

    constructor(public username: string,
        public firstname: string,
        public secondname: string,
        public password: string,
        public passwordConfirm: string,
        public email: string,
        public role: string) { }

}
