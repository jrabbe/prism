module.exports = function (grunt) {
    var path = require('path');

    grunt.loadNpmTasks('grunt-typescript');
    grunt.loadNpmTasks('grunt-express');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        express: {
            custom: {
                options: {
                    server: path.resolve('./js/lib/prism'),
                    port: 8080,
                    bases: 'js'
                }
            }
        },
        typescript: {
            base: {
                src: ['lib/**/*.ts'],
                dest: 'js',
                options: {
                    target: 'es5'
                }
            }
        },
        watch: {
            files: '**/*.ts',
            tasks: ['typescript']
        }
    });

    grunt.registerTask('default', ['express', 'watch']);
}
