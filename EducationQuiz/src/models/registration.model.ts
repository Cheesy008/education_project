export class RegistrationModel {

    constructor(public username: string,
        public firstname: string,
        public secondname: string,
        public password: string,
        public passwordConfirm: string,
        public email: string,
        public role: string) { }

}
export class RegistrationErrorsModel {

    constructor(public username: [],
        public first_name: [],
        public last_name: [],
        public password1: [],
        public password2: [],
        public email: [],
        public role: []) { }

}
