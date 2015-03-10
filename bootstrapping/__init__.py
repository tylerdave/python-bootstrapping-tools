import subprocess


class ShellError(RuntimeError):
    pass


class CurlError(ShellError):
    pass


def shell_command(command):
    # TODO: capture stdout / stderr
    p = subprocess.Popen(command.split())
    status = p.wait()
    if status !=0:
        # TODO: provide better error output
        raise ShellError('Shell command exited with an error.')

def curl_download(url, filename):
    command = 'curl -o {filename} {url}'.format(filename=filename, url=url)
    # TODO: capture stdout / stderr
    p = subprocess.Popen(command.split())
    status = p.wait()
    if status !=0:
        # TODO: get the actual error output
        raise CurlError('curl exited with an error.')


