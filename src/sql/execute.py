import mysql.connector
from mysql.connector.cursor import MySQLCursor

try:
    import cx_Oracle
except ModuleNotFoundError:
    pass


class Executor:
    def __init__(self, conn, verbose=False):
        self.conn = conn
        self.verbose = verbose

    def execute(self, filepath, commit):
        raise NotImplementedError


class OracleExecutor(Executor):
    def execute(self, filepath, commit=True):
        conn = self.conn
        cursor = conn.cursor()

        with open(filepath) as f:
            file = f.read()

        for line in file.split(';'):
            line = line.strip()

            # Skip empty command
            if line == '':
                continue

            try:
                cursor.execute(line)
            except Exception as exception:
                self.handle_exception(exception, line)

        if commit:
            conn.commit()

    def handle_exception(self, exception, line):
        """ Handle exception while executing a line.

            Raises all errors except when error code equals 942 when
            the command is a DROP statement.

        Args:
            exception: Exception raised.
            line: Current line.

        """
        error, = exception.args
        if line == '':  # Empty line
            pass
        else:
            if self.verbose:
                print(f'{"-" * 70}\n{line}\n{"-" * 70}')

            if not isinstance(exception, cx_Oracle.DatabaseError):
                raise exception
            elif error.code == 942 and 'drop' in line.lower():  # 942 should only occur in drop command
                pass
            else:
                raise exception


class MySqlExecutor(Executor):
    def execute(self, filepath, commit=True):
        conn = self.conn
        cursor = conn.cursor(buffered=True)

        with open(filepath) as f:
            file = f.read()

        for block in file.split(';'):
            block = block.strip()

            # Skip empty command
            if block == '':
                continue

            # Remove comment from lines
            lines = block.split('\n')
            block = '\n'.join([i for i in lines if not i.startswith('--')])

            try:
                cursor.execute(block)
            except Exception as exception:
                self._handle_exception(exception, block)

        if commit:
            conn.commit()

    @staticmethod
    def _handle_exception(exception, block):
        print(f'Exception occurred for command:\n{block}')
        raise exception


if __name__ == '__main__':
    # import sys
    #
    # from connect import connect
    # from credentials import username, password
    #
    # conn = connect(username, password)
    #
    # filepath = sys.argv[1]
    # execute_file(file_path=file_path, conn=conn, commit=True)
    pass